import pyautogui as pag
from time import sleep
# print(pag.position())

#screenshot
scr = pag.screenshot(region=(455,493,1000,1000))
scr.save('D:\Learn Python\Tool Python\Exercise\Pyautogui\#4 Take screenshots\img2.png')