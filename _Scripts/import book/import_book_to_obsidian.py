import os
import re
import argparse
import logging
import shutil
import pypdf
import ebooklib
from ebooklib import epub
from markdownify import markdownify as md

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Import the metadata function from your get_isbn_data script
try:
    from get_isbn_data import get_metadata
except ImportError:
    logging.warning("get_isbn_data.py not found in the same directory. Metadata will fallback to defaults.")
    def get_metadata(isbn):
        return {"ISBN-13": isbn, "Title": "Unknown Title", "Authors": ["Unknown Author"]}

def extract_isbn_from_filename(filename: str) -> str:
    """
    Identifies and returns a 10 or 13-digit ISBN from the filename.
    Strips out hyphens/spaces for a clean ID.
    """
    # Regex to find standard ISBN-10 or ISBN-13 patterns
    match = re.search(r'(97[89][- ]?)?\d{1,5}[- ]?\d{1,7}[- ]?\d{1,6}[- ]?[\dX]', filename, re.IGNORECASE)
    if match:
        clean_isbn = re.sub(r'[- ]', '', match.group(0).upper())
        if len(clean_isbn) in (10, 13):
            return clean_isbn
    return None

def write_obsidian_md(output_path: str, meta: dict, content: str):
    """
    Formats the extracted text into Obsidian Markdown, inserting YAML metadata 
    at the top of the file.
    """
    title = meta.get("Title", "Unknown Title")
    authors_list = meta.get("Authors", ["Unknown Author"])
    
    # Ensure it's a list, then format each author as an individual stringified backlink
    if isinstance(authors_list, str):
        authors_list = [authors_list]
        
    # Creates an array format: ["[[Author 1]]", "[[Author 2]]"]
    formatted_authors = "[" + ", ".join([f'"[[{author}]]"' for author in authors_list]) + "]"
    
    isbn = meta.get("ISBN-13", "")
    
    # Obsidian YAML Frontmatter
    frontmatter = (
        "---\n"
        f"tags: \"Book\"\n"
        f"Genre: \"[[{title}]]\"\n"
        f"author: {formatted_authors}\n"
        f"isbn: {isbn}\n"
        "---\n\n"
        f"# {title}\n\n"
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

def convert_txt_to_md(input_path: str, output_path: str, meta: dict):
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    write_obsidian_md(output_path, meta, content)
    return True

def convert_pdf_to_md(input_path: str, output_path: str, meta: dict):
    content = ""
    try:
        with open(input_path, 'rb') as pdfFile:
            pdfReader = pypdf.PdfReader(pdfFile)
            for i in range(len(pdfReader.pages)):
                pageObj = pdfReader.pages[i]
                text = pageObj.extract_text()
                if text:
                    content += f"\n\n## Page {i + 1}\n\n{text}"
        write_obsidian_md(output_path, meta, content)
        return True
    except Exception as e:
        logging.error("Error processing PDF %s: %s", input_path, e)
        return False

def convert_epub_to_md(input_path: str, output_path: str, meta: dict):
    content = ""
    book_folder = os.path.dirname(output_path)
    images_folder = os.path.join(book_folder, "images")
    
    try:
        book = epub.read_epub(input_path)
        
        # 1. Extract Images
        has_images = False
        for item in book.get_items_of_type(ebooklib.ITEM_IMAGE):
            if not has_images:
                os.makedirs(images_folder, exist_ok=True)
                has_images = True
                
            # Extract just the filename from the internal epub path
            img_filename = os.path.basename(item.get_name())
            img_filepath = os.path.join(images_folder, img_filename)
            
            with open(img_filepath, "wb") as img_file:
                img_file.write(item.get_content())
                
        if has_images:
            logging.info("Extracted images to: %s", images_folder)

        # 2. Extract Chapters
        chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        
        for i, chapter in enumerate(chapters):
            html_content = chapter.get_body_content().decode('utf-8', errors='ignore')
            markdown_text = md(html_content, heading_style="ATX").strip()
            
            # Clean up residual self-referential HTML/XHTML links
            markdown_text = re.sub(r'\[(.*?)\]\([^)]*\.xhtml[^)]*\)', r'\1', markdown_text)
            markdown_text = re.sub(r'\[(.*?)\]\([^)]*\.html[^)]*\)', r'\1', markdown_text)
            markdown_text = re.sub(r'\[(.*?)\]\([^)]*\.htm[^)]*\)', r'\1', markdown_text)
            
            # Clean up image links to point to the local 'images/' folder
            markdown_text = re.sub(
                r'!\[([^\]]*)\]\(([^)]+)\)', 
                lambda m: f"![{m.group(1)}](images/{os.path.basename(m.group(2))})", 
                markdown_text
            )
            
            if markdown_text:
                content += f"\n\n---\n\n## Section {i + 1}\n\n{markdown_text}"
                
        write_obsidian_md(output_path, meta, content)
        return True
    except Exception as e:
        logging.error("Error processing EPUB %s: %s", input_path, e)
        return False

def process_directory(input_folder: str, output_folder: str):
    """
    Finds files, filters by ISBN existence, fetches metadata, and processes conversions.
    Outputs each book into its own dedicated folder, then moves the source file to processed_books.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info("Created main output directory: %s", output_folder)

    # Create the processed books folder inside the input folder
    processed_folder = os.path.join(input_folder, "processed_books")
    os.makedirs(processed_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Skip directories (this will naturally skip the 'processed_books' folder)
        if not os.path.isfile(input_path):
            continue

        # 1. & 2. Find files and Identify if filename contains ISBN
        isbn = extract_isbn_from_filename(filename)
        if not isbn:
            logging.info("Skipped: '%s' (No valid ISBN found)", filename)
            continue

        logging.info("Processing '%s' (ISBN: %s)...", filename, isbn)
        
        # 3. Gather metadata from ISBN
        meta = get_metadata(isbn)
        
        # Format a safe base name from Book Title + ISBN
        safe_title = re.sub(r'[\\/*?:"<>|]', "", meta.get("Title", "Unknown_Title"))
        base_folder_name = f"{safe_title}_{isbn}".replace(" ", "_")
        
        # Create an individual folder for this specific book
        book_folder_path = os.path.join(output_folder, base_folder_name)
        os.makedirs(book_folder_path, exist_ok=True)
        
        # Set the markdown filename and final output path
        md_filename = f"{base_folder_name}.md"
        output_path = os.path.join(book_folder_path, md_filename)

        # 4. Convert file to markdown based on extension
        ext = os.path.splitext(filename)[1].lower()
        success = False
        
        if ext == '.txt':
            success = convert_txt_to_md(input_path, output_path, meta)
        elif ext == '.pdf':
            success = convert_pdf_to_md(input_path, output_path, meta)
        elif ext == '.epub':
            success = convert_epub_to_md(input_path, output_path, meta)
        else:
            logging.warning("Unsupported file type '%s' for file '%s'. Skipping.", ext, filename)
            continue
            
        # 5. Export and move to processed folder
        if success:
            logging.info("Exported successfully to: %s", output_path)
            try:
                processed_filepath = os.path.join(processed_folder, filename)
                shutil.move(input_path, processed_filepath)
                logging.info("Moved processed source file to: %s", processed_filepath)
            except Exception as e:
                logging.error("Failed to move file %s to processed directory: %s", filename, e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Import book files to Obsidian Markdown format.")
    parser.add_argument("input_folder", help="Folder path containing the source files (.epub, .pdf, .txt)")
    parser.add_argument("output_folder", help="Folder path to output the Obsidian .md files")
    
    args = parser.parse_args()
    
    logging.info("Starting batch conversion from %s to %s", args.input_folder, args.output_folder)
    process_directory(args.input_folder, args.output_folder)
    logging.info("Batch conversion complete.")