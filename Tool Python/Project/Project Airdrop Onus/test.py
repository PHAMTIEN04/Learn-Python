import pytesseract
from PIL import Image
import os
os.chdir("C:\Program Files\Tesseract-OCR")
a = pytesseract.image_to_data(Image.open("D:/Learn Python/Tool Python/Project/Project Airdrop Onus/test.png"))
print(a)