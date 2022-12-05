#!python3
#combines all the pdf inthe current working directory into a single pdf

import PyPDF2, os
#get all the PDF filenames
pdfFiles=[]
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter=PyPDF2.PdfFileWriter()

#loop through all the PDF files
for filename in pdfFiles:
    pdfFilesObj= open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFilesObj)
    # loop through all pages(except the first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj =pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#save the resulting pdf to a file
pdfOutput=open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
    