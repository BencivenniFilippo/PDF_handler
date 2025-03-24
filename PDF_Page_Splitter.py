import PyPDF2
import os

""" Common height for a document is 842
    If 4000 then 3 splits is ok"""

def split_pdf(input_path, output_path, num_splits):
    
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()
    
        page = reader.pages[0]
        width = page.mediabox.width
        height = page.mediabox.height
        print(height)

        split_height = height / num_splits

        for i in range(num_splits):
            new_page = page

            # Crop the page
            new_page.mediabox.upper_left = (0, height - (i + 1) * split_height)
            new_page.mediabox.lower_right = (width, height - i * split_height)

            # Add the cropped page to the writer
            writer.add_page(new_page)


        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    print(f"PDF split into {num_splits} parts and saved as '{output_path}'.")