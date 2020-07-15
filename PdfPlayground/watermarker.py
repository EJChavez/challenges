import PyPDF2

input_file = 'twopage.pdf'
watermark_file = 'wtr.pdf'
output_file = 'test.pdf'

x = 0
# opens our input file that we want to watermark
with open(input_file, "rb") as file_to_mark:
    pdf = PyPDF2.PdfFileReader(file_to_mark)
    # opens the file of our watermark and gets the 'page' aka our marking
    with open(watermark_file, "rb") as mark_to_add:
        watermark = PyPDF2.PdfFileReader(mark_to_add)
        first_page_watermark = watermark.getPage(0)
        # creates the object that will write our new watermarked pdf
        pdf_writer = PyPDF2.PdfFileWriter()
        # loops over the number of pages of our pdf, adds the watermark, and writes it to the new pdf variable
        while x < pdf.numPages:
            page_number = pdf.getPage(x)
            page_number.mergePage(first_page_watermark)
            pdf_writer.addPage(page_number)
            x = x + 1
        # opens and writes our new file
        with open(output_file, "wb") as file_created:
            # write the watermarked file to the new file
            pdf_writer.write(file_created)

def how_andrei_did_it():
    template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)

how_andrei_did_it()