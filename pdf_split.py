import argparse
import os
from PyPDF2 import PdfReader, PdfWriter
from copy import deepcopy

def split_page(original_page, split_direction):
    # Get the original page dimensions
    original_width = original_page.mediabox.width
    original_height = original_page.mediabox.height

    if split_direction == 'horizontal':
        # Create deep copies of the original page
        top_half = deepcopy(original_page)
        bottom_half = deepcopy(original_page)

        # Adjust the media boxes for the new pages
        # Top half: crop the bottom half
        top_half.mediabox.lower_left = (0, original_height / 2)
        top_half.mediabox.upper_right = (original_width, original_height)

        # Bottom half: crop the top half
        bottom_half.mediabox.lower_left = (0, 0)
        bottom_half.mediabox.upper_right = (original_width, original_height / 2)

        return top_half, bottom_half

    elif split_direction == 'vertical':
        # Create deep copies of the original page
        left_half = deepcopy(original_page)
        right_half = deepcopy(original_page)

        # Adjust the media boxes for the new pages
        # Left half: crop the right half
        left_half.mediabox.lower_left = (0, 0)
        left_half.mediabox.upper_right = (original_width / 2, original_height)

        # Right half: crop the left half
        right_half.mediabox.lower_left = (original_width / 2, 0)
        right_half.mediabox.upper_right = (original_width, original_height)

        return left_half, right_half

    # Default case: split based on the longest side
    if original_width > original_height:
        return split_page(original_page, 'vertical')
    else:
        return split_page(original_page, 'horizontal')		
def split_pages(input_pdf, page_ranges, split_direction):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    
    for page_num in range(total_pages):  # Process all pages
        original_page = reader.pages[page_num]
        
        # Check if the current page is in any of the specified ranges
        in_range = any(start - 1 <= page_num < end for start, end in page_ranges)
        
        if in_range:
            # Split the page if it's in the specified range
            first_half, second_half = split_page(original_page, split_direction)
            writer.add_page(first_half)
            writer.add_page(second_half)
        else:
            # Add the original page if it's not in the specified range
            writer.add_page(original_page)

    return writer

def main():
    parser = argparse.ArgumentParser(description="Split specified page ranges of a PDF into double pages.")
    parser.add_argument('-i', '--input', required=True, help='Input PDF file path')
    parser.add_argument('-f', '--from_page', type=int, nargs='+', required=True, help='Start page numbers for ranges')
    parser.add_argument('-to', '--to_page', type=int, nargs='+', required=True, help='End page numbers for ranges')
    parser.add_argument('--horizontal', action='store_true', help='Split pages horizontally')
    parser.add_argument('--vertical', action='store_true', help='Split pages vertically')

    args = parser.parse_args()

    if len(args.from_page) != len(args.to_page):
        print("Error: You must provide matching -f and -to arguments.")
        return

    # Create page ranges from the provided arguments
    page_ranges = list(zip(args.from_page, args.to_page))
    
    # Determine split direction
    if args.horizontal:
        split_direction = 'horizontal'
    elif args.vertical:
        split_direction = 'vertical'
    else:
        split_direction = 'auto'

    # Create output filename
    base_name = os.path.splitext(args.input)[0]
    output_pdf = f"{base_name}_split.pdf"

    # Split pages and write to new PDF
    writer = split_pages(args.input, page_ranges, split_direction)
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

    print(f"Output written to: {output_pdf}")

if __name__ == "__main__":
    main()