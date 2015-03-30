import os
from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = "."
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()

pdf_files.sort()

for filename in pdf_files:
    print("processing file: {0}".format(filename))
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(files_dir, "merged_full.pdf"))