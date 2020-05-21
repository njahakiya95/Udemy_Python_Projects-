import PyPDF2 

#Open document to watermark as a binary file
document = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

#Open watermarker template pdf as a binary file
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

#OVariable to hold the watermarked document
output = PyPDF2.PdfFileWriter()

#Loop over document and merge the watermarker pdf with each page of the input document
for i in range(document.getNumPages()):
	page = document.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	#Open a new file 
	with open('watermarked_output.pdf', 'wb') as file:
		output.write(file)