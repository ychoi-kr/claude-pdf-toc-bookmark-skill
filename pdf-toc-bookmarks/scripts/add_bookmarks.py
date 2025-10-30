#!/usr/bin/env python3
"""
Add bookmarks to PDF from TOC structure.
"""

import fitz
import sys
import os


def add_bookmarks(pdf_path, toc_list, page_offset, output_path):
    """
    Add bookmarks to PDF from TOC structure.
    
    Args:
        pdf_path: Path to input PDF
        toc_list: List of [level, title, page_number] entries
        page_offset: Offset between printed and actual PDF page numbers
        output_path: Path to output PDF
    """
    doc = fitz.open(pdf_path)
    
    # Apply page offset
    toc_with_offset = [
        [level, title, page + page_offset] 
        for level, title, page in toc_list
    ]
    
    # Set TOC
    doc.set_toc(toc_with_offset)
    
    # Save
    doc.save(output_path)
    doc.close()
    
    print(f"✅ Added {len(toc_list)} bookmarks to PDF")
    print(f"📁 Saved to: {output_path}")


if __name__ == "__main__":
    # This script is meant to be used as a library
    # Example usage in Python:
    # from add_bookmarks import add_bookmarks
    # 
    # toc = [
    #     [1, "Chapter 1", 10],
    #     [2, "Section 1.1", 11],
    # ]
    # add_bookmarks("input.pdf", toc, page_offset=4, output_path="output.pdf")
    
    print("This script should be imported and used as a library.")
    print("See SKILL.md for usage examples.")
