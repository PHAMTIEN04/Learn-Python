import pyautogui as pag
from time import sleep

# pos = pag.position()
# print(pos)
# pag.screenshot("test.png",region=(752,317,390,600))
#752,317
pag.PAUSE = 0.1
images = [
    {"file": "1.png", "confidence": 0.9, "region": (752,317,390,600)}, 
    {"file": "2.png", "confidence": 0.9, "region": (752,317,390,600)}, 
    {"file": "3.png", "confidence": 0.9, "region": (752,317,390,600)},  
    {"file": "4.png", "confidence": 0.9, "region": (752,317,390,600)},
    {"file": "5.png", "confidence": 0.9, "region": (752,317,390,600)},   
    {"file": "6.png", "confidence": 0.9, "region": (752,317,390,600)},   
]
#948,579

while True:    
    pos_play = pag.locateOnScreen("play.png",confidence=0.9,region=(752,317,390,600))
    
    if pos_play is not None:
        print("Play game!!!")
        pag.click(pos_play,interval=0.0)
        print("Đang đào vàng...")
        while True:
        #play 

    
            #daovang
            for img in images:
                pos = pag.locateOnScreen(image=img["file"],confidence=img["confidence"],region=img["region"])
                if pos is not None:
                    pag.click(pos,interval=0.0)
            #back
            pos_back = pag.locateOnScreen("back.png",confidence=0.9,region=(752,317,390,600))
            if pos_back is not None:
                pag.click(pos_back,interval=0.0)
                break
        print("Đã đào xong đợi 10p để tiếp tục!!!")
        sleep(600)
    
        