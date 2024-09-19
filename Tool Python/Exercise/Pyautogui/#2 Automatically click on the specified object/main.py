import pyautogui as pag
from time import sleep

image = "D:\Learn Python\Tool Python\Exercise\Pyautogui\#2 Automatically click on the specified object\setting.png"
pos = pag.locateOnScreen(image)
c_img = pag.click(pos)