#file handling functions
import docx

d = open('C:/Users/HP/Desktop/Literature Study/Python programming language/My-Daily-Python/file_handling/d.docx')
for f in d.paragraphs:
    print(d.text)
