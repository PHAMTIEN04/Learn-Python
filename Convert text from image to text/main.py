import cv2
import pytesseract

# Đường dẫn đến tệp hình ảnh bạn muốn đọc chữ từ đó
image_path = 'C:/Users/phamp/Downloads/imgatest.png'

# Đọc hình ảnh bằng OpenCV
image = cv2.imread(image_path)

# Chuyển đổi hình ảnh thành đen trắng (grayscale) để cải thiện việc nhận dạng
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sử dụng pytesseract để đọc chữ từ hình ảnh
text = pytesseract.image_to_string(gray_image)

# In ra kết quả đọc được
print(text)
