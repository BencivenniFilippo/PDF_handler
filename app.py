from PDF_Page_Scaler import enlarge_pdf
from PDF_Page_Splitter import split_pdf
import os

def main(input_path):
     
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file '{input_path}' does not exist.")
    
    input_dir = os.path.dirname(input_path)
    input_filename = os.path.basename(input_path)

    output_filename = '\\split_' + input_filename
    output_path = input_dir + output_filename

    split_pdf(input_path, output_path, 4)

main(r"G:\My Drive\Documenti\Statistical Modelling\Lessons\01_introduction.pdf")