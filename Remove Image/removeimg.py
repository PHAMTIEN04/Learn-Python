import numpy as np
import cv2
from PIL import Image
input_path = r'D:\Learn Python\Remove Image\input.jpg'
output_path = 'output.png'

input_image = cv2.imread(input_path)
output_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Chuyển đổi ảnh sang ảnh xám
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Áp dụng ngưỡng nhị phân để tách nền
_, mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV)

# Kiểm tra và chỉnh sửa kích thước mask nếu cần
if mask.shape[:2] != input_image.shape[:2]:
    mask = cv2.resize(mask, input_image.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# Áp dụng mask để loại bỏ nền
output_image = cv2.bitwise_and(output_image, output_image, mask=mask)

# Lưu ảnh kết quả
output_image = Image.fromarray(output_image)
output_image.save(output_path)
