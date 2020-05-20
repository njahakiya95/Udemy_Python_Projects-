import PyPDF2 
import sys

#list of user entered pdf files to be merged
inputs = sys.argv[1:]	

#pdf_mergercombines pdf files using PyPDF2 
def pdf_merger(pdf_list):	
	merger = PyPDF2.PdfFileMerger()	#user merger object 
	for pdf in pdf_list:			
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')	#new combined output pdf file

#call function 
pdf_merger(inputs)


