#!/usr/bin/env python3
"""
Extract table of contents pages from PDF as images for visual analysis.
"""

import fitz
import sys
import os


def extract_toc_images(pdf_path, toc_start_page, toc_end_page, output_dir):
    """
    Extract TOC pages as high-resolution images.
    
    Args:
        pdf_path: Path to input PDF
        toc_start_page: First TOC page (1-based)
        toc_end_page: Last TOC page (1-based)
        output_dir: Directory to save images
    """
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    
    for page_num in range(toc_start_page - 1, toc_end_page):
        page = doc[page_num]
        mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for high quality
        pix = page.get_pixmap(matrix=mat)
        
        output_path = os.path.join(output_dir, f"page_{page_num + 1:03d}.png")
        pix.save(output_path)
        print(f"Saved: {output_path}")
    
    doc.close()
    print(f"\n✅ Extracted {toc_end_page - toc_start_page + 1} TOC pages to {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python extract_toc_images.py <pdf_path> <start_page> <end_page> <output_dir>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])
    output_dir = sys.argv[4]
    
    extract_toc_images(pdf_path, start_page, end_page, output_dir)
