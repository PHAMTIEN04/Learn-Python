import pyautogui as pag
from time import sleep
# print(pag.position())

#click telegram
pag.click(1340,1060)
sleep(3)
#click search
pag.click(149,47)
sleep(3)
#send text
pag.typewrite("https://t.me/LayerAI_org")
sleep(5)
#click profile
pag.click(186,110)
sleep(3)
#click write message
pag.click(854,1006)
sleep(3)
#send message
pag.typewrite("Perfect")
pag.press("enter")