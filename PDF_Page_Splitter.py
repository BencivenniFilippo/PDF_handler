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
            new_page = reader.pages[0]

            # Crop the page
            new_page.mediabox.upper_left = (0, height - (i + 1) * split_height)
            new_page.mediabox.lower_right = (width, height - i * split_height)

            # Add the cropped page to the writer
            writer.add_page(new_page)


        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    print(f"PDF split into {num_splits} parts and saved as '{output_path}'.")



def main(input_path):
     
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file '{input_path}' does not exist.")
    
    input_dir = os.path.dirname(input_path)
    input_filename = os.path.basename(input_path)

    output_filename = '\\split_' + input_filename
    output_path = input_dir + output_filename

    split_pdf(input_path, output_path, 3)

main(r"G:\My Drive\Documenti\Statistical Modelling\01_introduction.pdf")


#     with open(input_path, 'rb') as input_file:
#         reader = PyPDF2.PdfReader(input_file)
# 
#         if len(reader.pages) > 1:
#             print('The PDF must have exactly 1 page to split')
#             return
#         
#         page = reader.pages[0]
#         height = page.mediabox.height
#         
#         if height < 
