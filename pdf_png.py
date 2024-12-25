import os
from pdf2image import convert_from_path

# Specify the directory containing your PDF files
pdf_dir = r"tst_data\certifs\OPEN CLASSROOMS"

# Specify the output directory for PNG files
output_dir = "images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through all PDF files in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        
        # Convert PDF to image
        images = convert_from_path(pdf_path)
        
        # Save the image as PNG
        for i, image in enumerate(images):
            png_file = os.path.splitext(pdf_file)[0] + ".png"
            png_path = os.path.join(output_dir, png_file)
            image.save(png_path, "PNG")
            print(f"Converted {pdf_file} to {png_file}")

print("Conversion completed!")
