import pyautogui as pag
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Hàm tìm kiếm hình ảnh với OpenCV
def find_image_opencv(template_path, region=None, confidence=0.8):
    screenshot = pag.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_loc if max_val >= confidence else None  # Ngưỡng độ tương đồng

# Hàm click vào vị trí với tốc độ nhanh
def find_and_click(image):
    pos = find_image_opencv(image["file"], image["region"], image["confidence"])
    if pos is not None:
        x, y = pos
        center_x = x + image["region"][0] + 25  # Điều chỉnh vị trí click
        center_y = y + image["region"][1] + 25
        pag.click(center_x, center_y, interval=0.0)

# Danh sách các hình ảnh cần tìm và confidence tương ứng
images = [
    {"file": "img1.png", "confidence": 0.8, "region": (733,231,380,600)},  # Confidence 0.8 cho img1
    {"file": "img2.png", "confidence": 0.9, "region": (733,231,380,600)},  # Nâng confidence lên 0.9 cho img2
    {"file": "img3.png", "confidence": 0.8, "region": (733,231,380,600)},  # Confidence 0.8 cho img3
    {"file": "img4.png", "confidence": 0.8, "region": (733,231,380,600)}   # Confidence 0.8 cho img4
]

# Sử dụng ThreadPoolExecutor để tăng số luồng xử lý đồng thời
with ThreadPoolExecutor(max_workers=8) as executor:  # Điều chỉnh max_workers nếu cần
    for i in range(200):  # Lặp lại 200 lần
        futures = [executor.submit(find_and_click, image) for image in images]
        
        # Đợi tất cả các luồng hoàn thành trước khi tiếp tục vòng lặp
        for future in futures:
            future.result()

# import pyautogui as pag

# pos = pag.position()
# print(pos)
# pag.screenshot("hihi.png",region=(733,231,380,600))