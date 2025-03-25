import PyPDF2
import os

def get_split_page_height(doc_path):
    try:
        with open(doc_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)

            page = reader.pages[0]

            height = page.mediabox.height
            denominator = 1000
            splits = height//denominator

            print(f'{os.path.basename(doc_path)}: {page.mediabox.height} - (splits: {splits} - height per split: {height//splits})') # print the base name of the file and it's length

            return (height//splits, splits)
        
    except Exception as e:
        print((f"Error reading {os.path.basename(doc_path)}: {e}"))
        return (900, 1)
    

""" Common height for a document is 842"""

def split_pdf(input_path, output_path, num_splits):
    
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()
    
        page = reader.pages[0]
        width = page.mediabox.width
        height = page.mediabox.height

        split_height = height / num_splits

        for i in range(int(num_splits)):
            new_page = page

            # Crop the page
            new_page.mediabox.upper_left = (0, height - (i + 1) * split_height)
            new_page.mediabox.lower_right = (width, height - i * split_height)

            # Add the cropped page to the writer
            writer.add_page(new_page)


        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    print(f"PDF split into {num_splits} parts and saved as '{output_path}'.")