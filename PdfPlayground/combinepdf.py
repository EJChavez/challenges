# merge dummy.pdf and twopage.pdf and tilt.pdf
import PyPDF2
import sys
# to use sys in pycharm I need to add the arguments in the parameters one by one apparently
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)