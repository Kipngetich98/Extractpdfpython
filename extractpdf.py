import pyPDF2
pdf = open("","rb") #insert the pdf link here
reader = pyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())

