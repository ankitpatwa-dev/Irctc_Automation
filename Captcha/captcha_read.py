from PIL import Image


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = Image.open("1.jpg","r")
# data = list(im.getdata())

data = pytesseract.image_to_string(im, config='')


print(data)