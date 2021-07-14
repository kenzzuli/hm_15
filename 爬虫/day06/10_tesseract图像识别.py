import pytesseract
from PIL import Image

image = Image.open("./ocr.png")
print(pytesseract.image_to_string(image))
# This is some text, written in Arial, that will be read by
# Tesseract. Here are some symbols: !@#$%*&"*()
