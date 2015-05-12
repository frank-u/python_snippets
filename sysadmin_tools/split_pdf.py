import sys
from os.path import splitext, basename
from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf(fn):
    input_pdf = PdfFileReader(open(fn, "rb"))
    filename = splitext(basename(fn))[0]

    for i in range(input_pdf.numPages):
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(i))
        with open("{0}-p{1}.pdf".format(filename, i), "wb") as outputStream:
            output.write(outputStream)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        split_pdf(sys.argv[1])
    else:
        print("No filename in argument provided")
