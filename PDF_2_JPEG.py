from pdf2image import convert_from_path
from glob import glob
import os

###### Need to install poppler and pdf2image#####
# https://pdf2image.readthedocs.io/en/latest/installation.html


# Folder with PDFs
pdf_dir = r"N:\projects\2021\215324C195314 APS Delano 10 Rebuild Arch & Bio Survey (1.BIO)\Biology\Graphics-GIS\Images"

# If multipage PDF input: 1
# If single page PDF input: 2
pdf_type = 2

# JPEG Dots Per Inch (DPI)
dpi = 300

#############################################################################
pdfs = glob(pdf_dir + "\*.pdf")
len(pdfs)

os.chdir(pdf_dir)


def convert_pdf(pdf_type):
    if pdf_type == 1:
        for pdf in pdfs:
            pages = convert_from_path(pdf, dpi)
            for i, page in enumerate(pages):
                file_name = pdf[:-4] + "_" + str(i + 1) + ".jpg"
                page.save(file_name, "JPEG")
    elif pdf_type == 2:
        for pdf in pdfs:
            pages = convert_from_path(pdf, dpi)
            for page in pages:
                page.save(pdf[:-4] + ".jpg", "JPEG")
    return


convert_pdf(pdf_type)
#################################################################################

# Remove unneeded PDFs
for pdf in pdfs:
    os.remove(pdf)