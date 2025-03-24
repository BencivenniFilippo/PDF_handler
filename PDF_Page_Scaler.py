import PyPDF2

def enlarge_pdf(input_path, output_path, scale_factor=1.2):
    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Iterate through each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]

            original_width = page.mediabox.width
            original_height = page.mediabox.height

            new_width = original_width * scale_factor
            new_height = original_height * scale_factor

            # Set the new dimensions
            page.mediabox.upper_right = (new_width, new_height)

            writer.add_page(page)

        # Save the modified PDF to the output path
        with open(output_path, "wb") as output_file:
            writer.write(output_file)


# enlarge_pdf("input.pdf", "output.pdf", scale_factor=1.2)