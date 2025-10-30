# PDF TOC to Bookmarks Skill - Usage Guide

## Overview

This skill enables Claude to efficiently extract table of contents from PDF pages and create clickable bookmarks using visual analysis instead of error-prone text parsing.

## Installation

1. Download `pdf-toc-bookmarks.skill` file
2. In Claude.ai, go to Settings → Skills
3. Click "Import Skill" and upload the .skill file
4. The skill is now available for use

## How It Works

The skill follows a 5-step workflow:

1. **Extract TOC Pages as Images** - High-resolution page rendering
2. **Visual Analysis** - Claude reads TOC structure from images
3. **Calculate Page Offset** - Align printed vs PDF page numbers
4. **Add Bookmarks** - PyMuPDF creates hierarchical navigation
5. **Verify & Deliver** - Test bookmarks and provide download

## Example Usage

### Simple Request
```
User: "Add bookmarks to this PDF based on the table of contents"
```

### With Details
```
User: "This PDF has a table of contents on pages 10-16. Can you add 
clickable bookmarks so I can navigate easily?"
```

### What Claude Will Do

1. Extract TOC pages (10-16) as images
2. Show you the images and ask to verify TOC structure
3. Transcribe the TOC into a structured list
4. Calculate the page offset (e.g., 4 pages)
5. Add bookmarks to PDF using PyMuPDF
6. Provide download link to the bookmarked PDF

## Key Benefits

✅ **Vision-Based**: More accurate than text parsing  
✅ **Fast**: 10-15 minutes vs 30-60 minutes traditional methods  
✅ **Hierarchical**: Proper nesting (chapters, sections, subsections)  
✅ **Automatic Offset**: Handles printed vs PDF page number differences  

## Technical Details

### Scripts Included

1. **extract_toc_images.py** - Extracts TOC pages as high-res images
2. **add_bookmarks.py** - Adds bookmarks to PDF with offset support

### Requirements

- PyMuPDF (fitz) - already available in Claude's environment
- Works with any PDF containing printed table of contents

### Limitations

- Requires visual TOC pages in PDF
- User must specify which pages contain TOC
- Complex multi-column TOCs may need manual verification

## Tips for Best Results

1. **Know your TOC page range** - Check PDF beforehand
2. **Verify offset** - Test one bookmark to confirm accuracy
3. **Review structure** - Ensure hierarchy levels are correct
4. **Use descriptive titles** - Keep original TOC text exactly

## Support

For issues or improvements, contact the skill creator or modify the SKILL.md file to customize behavior.
