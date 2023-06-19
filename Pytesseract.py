import re
from pdf2image import convert_from_path
from pytesseract import image_to_string, pytesseract
 
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Store Pdf with convert_from_path function
images = convert_from_path('EN 0003 23.pdf', 
                            poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')
#page = int(input())
data = image_to_string(images[2]).splitlines() #split text to list
while("" in data):  #remove blank data in list (blank line)
    data.remove("")

regex = '^[-]|^\d'
for i in data:
    if re.search(regex,i):
        print(i.split())



#print(type(image_to_string(images[2])))
   
      # Save pages as images in the pdf
    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')