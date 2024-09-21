import pyautogui as pag
import time
import cv2
import numpy as np
from PIL import ImageGrab  # or use pag.screenshot if needed

pag.PAUSE = 0.001  # Minimize pauses for faster actions

# Load images using OpenCV
images = [
    {"file": cv2.imread("1mini.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.9, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("1minit.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.9, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("1tree.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.6, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("2tree.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.5, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("3tree.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.6, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("4tree.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.6, "region": (645, 272, 600, 180)},
    {"file": cv2.imread("bird.png", cv2.IMREAD_GRAYSCALE), "confidence": 0.5, "region": (645, 272, 600, 180)}
]

def capture_screen(region):
    left, top, width, height = region
    right = left + width  # Calculate right boundary
    bottom = top + height  # Calculate bottom boundary
    
    # Now grab the correct region
    screen = ImageGrab.grab(bbox=(left, top, right, bottom))  # (left, top, right, bottom)
    screen_np = np.array(screen)  # Convert to numpy array
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)  # Convert to grayscale for faster processing
    return screen_gray

while True:
    for img in images:
        # Capture the region of the screen to search in
        screen = capture_screen(img["region"])
        
        # Perform template matching
        result = cv2.matchTemplate(screen, img["file"], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # Check if confidence is high enough
        if max_val >= img["confidence"]:
            pos_left = max_loc[0] + img["region"][0]  # Adjust for region offset
            if pos_left <= 800:
                pag.keyDown("space")
                # Optionally adjust the sleep duration here for jump handling
                time.sleep(0.2 )
                pag.keyUp("space")
