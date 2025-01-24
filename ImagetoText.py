import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" #Copy the tesseract.exe file path and paste

def convert():
    try:
        img=Image.open('pic.png') #Your image name
    except FileNotFoundError:
        print("File not found")
        return
    try:
        text= pytesseract.image_to_string(img)
    except pytesseract.TesseractError as e:
        print(f'Error:{e}')
        return    
    print(text)
convert()    
