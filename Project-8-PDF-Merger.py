import os #for finding files
from PyPDF2 import PdfMerger #this module helped for merging pdf
merge_file = PdfMerger() #this is a class present in the module
a = os.listdir() #it creates the directories of the list
for i in a:
    if i.endswith(".pdf"):
        merge_file.append(i)
name=input("give the name for the merged file:")
merge_file.write(f"{name}") # it is important and gives the name for the new file
merge_file.close() # it closes the pdf
