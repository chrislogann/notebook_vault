import os
import shutil
import argparse

"""
Script exports markdown (.md) files from an Obsidian notebook folder to a target folderpath.
One can download all files or filter by criteria like a tag.
"""

def get_md_files(source_folder):
    """Recursively search for .md files in a directory."""
    md_files = []
    for root, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(".md"):
                md_files.append(os.path.join(root, filename))
    return md_files

def filter_md_files(md_files, filter_criteria):
    """Filter files based on the presence of a specific string."""
    if not filter_criteria:
        return md_files
        
    filtered_files = []
    for file in md_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if filter_criteria in content:
                    filtered_files.append(file)
        except Exception as e:
            print(f"Warning: Could not read '{file}'. Error: {e}")
            
    return filtered_files

def copy_md_files(md_files, target_folder):
    """Copy markdown files to target folderpath."""
    os.makedirs(target_folder, exist_ok=True)
    for file in md_files:
        shutil.copy(file, target_folder)

def export_notes(source_folder, target_folder, filter_criteria=None):
    """Core logic to execute the export process."""
    md_files = get_md_files(source_folder)
    filtered_files = filter_md_files(md_files, filter_criteria)
    copy_md_files(filtered_files, target_folder)
    
    print(f"Exported {len(filtered_files)} files to '{target_folder}'.")

def main():
    """Parses terminal arguments and runs the export process."""
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Export Markdown files from an Obsidian vault.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Define positional arguments (required)
    parser.add_argument("source", help="The path to your source Obsidian vault folder")
    parser.add_argument("target", help="The path to your target export folder")
    
    # Define optional arguments
    parser.add_argument(
        "-f", "--filter", 
        help="Optional text or tag to filter by (e.g., '#important')", 
        default=None
    )
    
    # Parse the arguments from the terminal
    args = parser.parse_args()
    
    # Execute the script with the provided arguments
    export_notes(args.source, args.target, args.filter)

if __name__ == "__main__":
    main()