import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image = cv2.imread('t.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
a = pytesseract.image_to_string(image)


print(a)