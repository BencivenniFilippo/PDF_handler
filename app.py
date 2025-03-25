from PDF_Page_Scaler import enlarge_pdf
from PDF_Page_Splitter import split_pdf, get_split_page_height
import os
from pathlib import Path

def main(dir_path):
     
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")

    for file_name in os.listdir(dir_path):

        output_filename = Path("split") / f"split_{file_name}"
        output_path = Path(dir_path) / output_filename

        file_path = Path(dir_path) / file_name
        split_page_height, splits = get_split_page_height(file_path)

        if split_page_height < 1800:
            print(splits)
            split_pdf(file_path, output_path, splits)

        # Too big pages
        else:
            split_pdf(file_path, output_path, splits+1)
        

if __name__ == '__main__':
    main(r"G:\My Drive\Documenti\Statistical Modelling\Lessons")