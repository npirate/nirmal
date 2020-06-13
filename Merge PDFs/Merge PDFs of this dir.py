#pip install PyPDF2

import os

from PyPDF2 import PdfFileMerger

os.chdir(r'C:\Users\nimals\Google Drive\Python Projects\Merge PDFs')

x = [a for a in os.listdir('.') if a.endswith(".pdf")]

#print (x)

merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open(input("Give Output Name:"), "wb") as fout:
    merger.write(fout)
    print ('Output generated')