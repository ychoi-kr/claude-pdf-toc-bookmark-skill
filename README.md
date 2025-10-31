# PDF TOC Bookmark Skill for Claude
This Claude Skill automatically adds bookmarks to a PDF file based on its table of contents (TOC).

## Overview
The skill analyzes the text of a PDF, detects the table of contents, and inserts bookmarks that correspond to the chapter and section titles.  
It's designed for quick document navigation and works well for books, reports, and long research papers.

> 💡 You don't need to mention the skill name explicitly — Claude will automatically use it when your request is relevant.

---

## Why Use This Skill?

- **🎯 More Accurate with Vision**  
  Uses Claude's multimodal capabilities to visually read TOC pages, avoiding the errors and trial-and-error common with rule-based text parsing

- **📐 Handles Page Offsets Correctly**  
  Includes best practices for calculating page number offsets (e.g., when "page 1" in the book is actually page 15 in the PDF), ensuring bookmarks link to the right locations

- **⚡ Saves Time and Tokens**  
  Automates a task that would otherwise require manual work or extensive prompt engineering, reducing both time and API costs through a proven workflow

---

## How to Use

1. **Download the skill package**  
   Get the latest release from:  
   [https://github.com/ychoi-kr/claude-pdf-toc-bookmark-skill/releases](https://github.com/ychoi-kr/claude-pdf-toc-bookmark-skill/releases)

2. **Install the skill in Claude**  
   - Open **Claude Settings → Features → Skills**  
   - Click **Upload Skill** and select the downloaded `pdf-toc-bookmarks.zip` file  
   - Enable the uploaded skill

3. **Ask Claude to process your PDF**  
   In chat, simply upload a PDF and say something like:  
   > “Can you add bookmarks based on the table of contents?”  

   (You don’t need to reference the skill name directly.)

4. **Download the updated PDF**  
   After processing, Claude will provide a new PDF file with bookmarks added.

---

## Notes

- The skill works accurately for most PDFs.  
- Occasionally, minor adjustments may be needed if:
  - The TOC text is not clearly recognized
  - The document lacks numbered section headers or has unusual formatting  
- You can manually fix such bookmarks or ask Claude to correct them afterward.

---

## Author

**Yong Choi**  
- GitHub: [@ychoi-kr](https://github.com/ychoi-kr)  
- Website: [https://ychoi.kr](https://ychoi.kr)

---

## License

MIT License
