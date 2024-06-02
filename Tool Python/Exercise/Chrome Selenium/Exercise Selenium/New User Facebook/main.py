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
def set_up():
    options = Options()
    chrome_prefs = {
        "profile.default_content_setting_values": {"images": 1}
    }
    #1die
    options.add_experimental_option("prefs", chrome_prefs)
    options.add_argument(f"--user-data-dir=D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/Facebook Account/Account 2")
    options.add_argument('--disable-notifications')
    driver = Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver
# Login
def login(driver):
    try:
        driver.get("https://www.facebook.com/")
        sleep(111110.5)
        path = "D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/account.txt"
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
    except Exception as e:
        print("Login Error!!!")
        print(e)
        exit()

def Get_ID_New_User(driver):
# Get ID New User
    try:
        driver.get("https://www.facebook.com/groups/146473906768401/members")
        x = 17
        while True:
            try:
                f = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[{x}]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a")
                break
            except:
                print("Bruceforce x:",x)
                x = x + 1       
        list_id = []
        for i in range(10):
            f = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[{x}]/div/div[2]/div/div[{i+1}]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a")
            rg = re.compile(r"user(.*)")
            crg = rg.search(f.get_attribute('href'))
            list_id.append(crg.group(1))
        print("Get ID Sussccess!!!")
        return list_id
    except Exception as e:
        print("Get ID Error!!!")
        print(e)
        exit()
# Check User trung lap
def check_user(list_id):
    try:
        list_id_old = []
        path = "D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/id.txt"
        with open(path,"r") as ac_r:
            a = ac_r.read()
            ac_r.close()

        list_id_old = a.split("\n")
        with open(path,"w") as ac_r:
            for i in list_id:
                if str(i) not in list_id_old:
                    ac_r.write(str(i) + '\n')
            ac_r.close()
        
        with open(path,"r") as ac_r:
            a = ac_r.read()
            ac_r.close()

        list_id_old = a.split("\n")
        return list_id_old
    except Exception as e:
        print("Check User Error!!!")
        print(e)
        exit()
# print(list_id)
# # sleep(100)
def Add_Friend(driver,id):
    try:    
        driver.get(f"https://www.facebook.com{id}")
        sleep(2)
        f = driver.find_element(By.CLASS_NAME,"x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft")
        if(f.text == "Add friend") or (f.text == "Thêm bạn bè"):
            f.click()
            print("Add Friend thanh cong!!!")
        sleep(2)
    except:
        print("Khong co nut Add Friend!!!")
def send_messages(driver,list_id_old):
    try:
        for i in list_id_old:
            if i !='':# Add Friend
                Add_Friend(driver,i)
                try:
                    driver.get(f"https://www.facebook.com/messages/t{i}")
                    sleep(3)

                    t1 = random.choice(["Chào bạn!","Hi bạn","Chào bạn","Hello bạn"])
                    driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys(t1,Keys.ENTER)
                    sleep(3)
                    driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn mới tải APP Onus phải không ạ!",Keys.ENTER)
                    sleep(3)
                    driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Mình là Đối Tác Onus có nhiệm vụ hỗ trợ và hướng dẫn người mới vào nhóm",Keys.ENTER)
                    sleep(3)
                    driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn đã nhận voucher 300k trải nghiệm Onus chưa ạ! Nếu chưa bạn làm theo các bước dưới đây nha",Keys.ENTER)
                    sleep(3)                       
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]").click()
                    sleep(3)
                    open_windows = gw.getWindowsWithTitle("Open")

                    if open_windows:

                        open_window = open_windows[0]
                        open_window.activate()

                        sleep(3)

                        file_path = r"D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\New User Facebook\voucher.jpg"

                        pyautogui.write(file_path)
                        sleep(0.5)


                        pyautogui.press("enter")
                        sleep(0.5)
                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[2]/div").click()
                    else:
                        print("Window with the title 'Open' not found.")
                    sleep(3)
                    driver.find_element(By.XPATH,"//p[contains(@class, 'xat24cr xdj266r')]").send_keys("Bạn làm xong gửi mình ID Onus để mình tặng voucher và mời vào nhóm Tín Hiệu Onus nha",Keys.ENTER)
                    sleep(3)
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]").click()
                    sleep(3)
                    open_windows = gw.getWindowsWithTitle("Open")

                    if open_windows:

                        open_window = open_windows[0]
                        open_window.activate()

                        sleep(3)

                        file_path = r"D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\New User Facebook\voucher1.png"

                        pyautogui.write(file_path)
                        sleep(0.5)


                        pyautogui.press("enter")
                        sleep(0.5)
                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[2]/div").click()
                    else:
                        print("Window with the title 'Open' not found.")
                    sleep(3)
                    print(f"ID:{i} Sussccess")
                except Exception as e:
                    print(f"ID:{i} Error!!")

            else:
                print("Messages hoan tat!!!")
            
    except:
        print("Messages Error!!!")
        
    print("Wait 1 hour for it to run automatically again!!!")
    sleep(10)
    driver.close()

def main():
    while True:
        driver = set_up()
        login(driver)
        get_id = Get_ID_New_User(driver)
        check = check_user(get_id)
        send_messages(driver,check)
        sleep(3600)

if __name__ == "__main__":
    main()
