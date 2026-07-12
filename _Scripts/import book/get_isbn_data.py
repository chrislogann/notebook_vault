import isbnlib
import logging

"""
Script get_isbn_data returns metadata from a given ISBN.
"""

def get_metadata(isbn: str) -> dict:
    """
    Returns metadata from an ISBN.
    Data is from package isbnlib.

    Params:
    isbn (str): Unique id for a specific book

    Returns:
    dict: Metadata pertaining to the given ISBN number.
    """
    
    try:
        # Fetch metadata using the OpenLibrary service
        meta = isbnlib.meta(isbn, service="openl")
        logging.debug("Found metadata for ISBN %s from isbnlib", isbn)
        
    except isbnlib.ISBNLibException as e:
        # Catching specific isbnlib exceptions to avoid swallowing unrelated errors
        meta = None
        logging.warning("isbnlib cannot find or validate ISBN %s. Error: %s", isbn, e)

    # Fallback response if metadata wasn't found
    if not meta:
        meta = {
            "ISBN-13": isbn,
            "Title": "Unknown Title",
            "Authors": ["Unknown Author"]
        }
        logging.debug("ISBN %s not found. Using fallback dictionary.", isbn)

    # Note: If you plan to cache this, the caching logic should go here.
    # logging.debug("Setting cache for ISBN metadata for ISBN %s", isbn)
    
    return meta