# pdf-suite
Small CLI scripts for easy PDF editing

Requires PyPDF2, made on Windows 10 with Python 3.12.3

Made up of probably Python3 scripts which make it wasy to quickly do common procedures you might need to do to make your PDF what you want it to be without using bloated software.

---

## Usage
1. Make sure python is installed
2. Install PyPDF2 with `pip install pypdf2`
3. Clone this repo
4. Use CMD or other terminal app (Powershell) and navigate to where this repo was cloned `cd [PATH]/pdf-suite`
5. Using the terminal, execute the scripts `py [SCRIPT NAME].py -i [INPUT PDF PATH] [OPTIONS]`

## Features
### Current list of tools:
- pdf_split - Splits the desired range/ranges of pages in half horizontally or vertically, useful for splitting up photos of double pages
  - `-f [PAGE NUM] -to [PAGE NUM]` to add a range or multiple ranges
  - `[-h OR -v]` to force horizntal or vertical splitting. By default will split whichever side is longest
  - Will use scaling to make sure the new pages are the same size as the regular pages
- pdf_del - Deletes the desired range/ranges of pages, useful for removing duplicates or remnants such as title pages, if those are not desired
  - `-f [PAGE NUM] -to [PAGE NUM]` to add a range or multiple ranges 

### Planned tools:
- pdf_easy_text - Will extract all embedded text and make it easy to make small changes such as spellchecking or adding special characters and then add it back
- pdf_compress - Crunch down common colors and use other algorithms to compress the size of the PDF

## Other tools
I recommend checking out [ocrmypdf](https://github.com/ocrmypdf/OCRmyPDF) for very good OCR for PDFs
