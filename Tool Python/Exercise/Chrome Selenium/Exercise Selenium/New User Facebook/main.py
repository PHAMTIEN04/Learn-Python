from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import os
from pynput.keyboard import Key,Controller
import random
import pyautogui
import pygetwindow as gw
options = Options()
chrome_prefs = {
    "profile.default_content_setting_values": {"images": 1}
}
options.add_experimental_option("prefs", chrome_prefs)
options.add_argument(f"--user-data-dir=D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/Facebook account/Account 0")
options.add_argument('--disable-notifications')
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div /div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[2]/ div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
# Login
driver.get("https://www.facebook.com/")
sleep(0.5)
path = os.getcwd() + "\\New User Facebook\\account.txt"
with open(path,"r") as ac_r:
    read = ac_r.read()
    ac_r.close()
r_a = re.compile(r"(.*?)\|")
r_p = re.compile(r"\|(.*)")
account = r_a.findall(read)
password = r_p.findall(read)
if driver.title == "Facebook – log in or sign up":
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys(account)
    driver.find_element(By.XPATH,"//*[@id='pass']").send_keys(password,Keys.ENTER)
sleep(0.5)
if driver.title != "Facebook – log in or sign up":
    print("Login Sussccess!!!")

sleep(3)

# Get ID New User
driver.get("https://www.facebook.com/groups/146473906768401/members")
# check xpath

xpath = ""
# check = False
x = 1
while True:
    try:
        for i in range(10):
            f = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[{x}]/div/div[2]/div/div[{i+1}]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a")
        break
    except:
        print("Bruceforce x:",x)
        x = x + 1    
list_id = []
for i in range(10):
    # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[18]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
    f = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[{x}]/div/div[2]/div/div[{i+1}]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a")
    rg = re.compile(r"user(.*)")
    crg = rg.search(f.get_attribute('href'))
    list_id.append(crg.group(1))

# Check User trung lap
list_id_old = []
path = os.getcwd() + "\\New User Facebook\\id.txt"
with open(path,"r") as ac_r:
    a = ac_r.read()
    ac_r.close()

list_id_old = a.split("\n")
print(list_id_old)
with open(path,"w") as ac_r:
    for i in list_id:
        if str(i) not in list_id_old:
            ac_r.write(str(i) + '\n')
    ac_r.close()
    
with open(path,"r") as ac_r:
    a = ac_r.read()
    ac_r.close()

list_id_old = a.split("\n")
print(list_id_old)

# print(list_id)
# # sleep(100)
try:
    for i in list_id_old:
        if i !='':# Add Friend
            driver.get(f"https://www.facebook.com{i}")
            sleep(2)
            try:
                f = driver.find_element(By.CLASS_NAME,"x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft")
                print(f.text)
                if(f.text == "Add friend"):
                    f.click()
                    print("Add Friend thanh cong!!!")
                
            except:
                print("Khong co nut Add Friend!!!")
    
            try:
                driver.get(f"https://www.facebook.com/messages/t{i}")
                sleep(0.5)

                t1 = random.choice(["Chào bạn!","Hi bạn","Chào bạn","Hello bạn"])
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys(t1,Keys.ENTER)
                sleep(3)
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn mới tải APP Onus phải không ạ!",Keys.ENTER)
                sleep(3)
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Mình là Đối Tác Onus có nhiệm vụ hỗ trợ và hướng dẫn người mới vào nhóm",Keys.ENTER)
                sleep(3)
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn làm theo các bước dưới đây để mình có thể dễ dàng hỗ trợ bạn hơn nha",Keys.ENTER)
                sleep(3)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/div").click()
                sleep(3)
                open_windows = gw.getWindowsWithTitle("Open")

                if open_windows:

                    open_window = open_windows[0]
                    open_window.activate()

                    sleep(0.5)

                    file_path = os.getcwd() + "\\New User Facebook\\1.jpg"

                    pyautogui.write(file_path)
                    sleep(0.5)


                    pyautogui.press("enter")
                    sleep(3)
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div").click()
                else:
                    print("Window with the title 'Open' not found.")
                sleep(0.5)
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("À với bên mình đang có chương trình hỗ trợ người mới khi hoàn thành các bước ở trên sẽ được nhận free Voucher Futures 200k",Keys.ENTER)
                sleep(3)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/div").click()
                sleep(3)
                open_windows = gw.getWindowsWithTitle("Open")

                if open_windows:

                    open_window = open_windows[0]
                    open_window.activate()

                    sleep(0.5)

                    file_path = os.getcwd() + "\\New User Facebook\\voucher.jpg"
                    pyautogui.write(file_path)
                    sleep(0.5)


                    pyautogui.press("enter")
                    sleep(3)
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div").click()
                else:
                    print("Window with the title 'Open' not found.")
                sleep(3)
                driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn làm xong gửi mình ID Onus để mình tặng voucher và mời vào nhóm Tín Hiệu Onus nha",Keys.ENTER)
                print(f"ID:{i} Sussccess")
            except Exception as e:
                print(f"ID:{i} Error!!")

        else:
            print("Messages hoan tat!!!")
            
except Exception as e:
    print("Messages Error!!!")
    print(e)
sleep(1000)
driver.close()
