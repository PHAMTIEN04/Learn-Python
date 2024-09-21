import pyautogui as pag
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Image search function with OpenCV
def find_image_opencv(template_path, region=None, confidence=0.8):
    screenshot = pag.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_loc if max_val >= confidence else None  # Similarity threshold

# The jaw clicks into place at a fast speed
def find_and_click(image):
    pos = find_image_opencv(image["file"], image["region"], image["confidence"])
    if pos is not None:
        x, y = pos
        center_x = x + image["region"][0] + 25  # Adjust click position
        center_y = y + image["region"][1] + 25
        pag.click(center_x, center_y, interval=0.0)

# List of images to search for and corresponding confidence
images = [
    {"file": "img1.png", "confidence": 0.8, "region": (733,231,380,600)}, 
    {"file": "img2.png", "confidence": 0.9, "region": (733,231,380,600)}, 
    {"file": "img3.png", "confidence": 0.8, "region": (733,231,380,600)},  
    {"file": "img4.png", "confidence": 0.8, "region": (733,231,380,600)}  
]

# Use ThreadPoolExecutor to increase the number of concurrent threads
with ThreadPoolExecutor(max_workers=8) as executor:  # c
    for i in range(200):  
        futures = [executor.submit(find_and_click, image) for image in images]
        

        for future in futures:
            future.result()

# import pyautogui as pag

# pos = pag.position()
# print(pos)
# pag.screenshot("hihi.png",region=(733,231,380,600))