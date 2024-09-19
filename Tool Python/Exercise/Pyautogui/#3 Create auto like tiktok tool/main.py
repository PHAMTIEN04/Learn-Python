import pyautogui as pag
from time import sleep

#get mouse position syntax : pag.position()
# pos = pag.position()
# print(pos)

# click chrome
pag.click(1246,1063)
sleep(3)
# new tab
pag.click(1717,14)
sleep(3)
# click search
pag.click(245,59)
pag.typewrite("tiktok.com/@chenniishere/video/7406303262850256136")
pag.press("enter")
sleep(5)
# click heart
for i in range(2):
    pag.click(1000,742)
