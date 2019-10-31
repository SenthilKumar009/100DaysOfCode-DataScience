import PyPDF2
import sys

inputs = sys.argv[1:]

def pdfCombiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    
    merger.write('superPDF.pdf')
#with open('sample.pdf', 'rb') as file1:

pdfCombiner(inputs)