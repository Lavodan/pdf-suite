import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def delete_pages(input_pdf, from_page, to_page, output_pdf):
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add pages to the writer, skipping the specified range
    for i in range(len(reader.pages)):
        if i < from_page - 1 or i > to_page - 1:
            writer.add_page(reader.pages[i])

    # Write the output PDF
    with open(output_pdf, 'wb') as f:
        writer.write(f)

def main():
    parser = argparse.ArgumentParser(description='Delete pages from a PDF file.')
    parser.add_argument('-i', '--input', required=True, help='Input PDF file path')
    parser.add_argument('-f', '--from_page', type=int, required=True, help='Page number to start deleting from (inclusive)')
    parser.add_argument('-to', '--to_page', type=int, required=True, help='Page number to stop deleting at (inclusive)')
    
    args = parser.parse_args()

    input_pdf = args.input
    from_page = args.from_page
    to_page = args.to_page

    # Validate page numbers
    if from_page < 1 or to_page < 1 or from_page > to_page:
        print("Invalid page numbers. Ensure that from_page and to_page are positive and from_page <= to_page.")
        return

    # Create output file path
    output_pdf = f"{os.path.splitext(input_pdf)[0]}_del.pdf"

    # Delete pages and create new PDF
    delete_pages(input_pdf, from_page, to_page, output_pdf)
    print(f"Output saved to: {output_pdf}")

if __name__ == '__main__':
    main()
