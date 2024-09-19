import pyautogui as pag
from time import sleep
#get mouse position syntax : pag.position()
# pos = pag.position()
# print(pos)
#Move mouse to location and click syntax : pag.click(x,y)
# click = pag.click(17,106)
# print(click)

##refresh 

##click chrome
c_chrome = pag.click(1277,1061)
sleep(3)

##click refresh 3 times

for i in range(3):
    pag.click(92,58)
    sleep(3)
