import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
# with open("account.txt","r") as ac_r:
#     read = ac_r.read()

#     r_a = re.compile(r"(.*?)\|")
#     r_p = re.compile(r"\|(.*?\w+)")
#     account = r_a.findall(read)
#     password = r_p.findall(read)
    
#     print("Account :",account)
#     print("Password :",password)
# with open("account.txt","+a") as ac_w:
#     acc_new = str(input("Nhap account: "))
#     pass_new = str(input("Nhap password: "))
#     write = ac_w.write("\n"+acc_new + "|" + pass_new)
#     ac_w.close()
options = Options()
location = os.getcwd()
options.add_argument(f"--user-data-dir={location}\Facebook account\Account 4")
options.add_argument('--disable-notifications')
driver = Chrome(options=options)
driver.implicitly_wait(10)
#  //*[@id="mount_0_0_No"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[23]/div/div[2]/div/div[1]
driver.get("https://www.facebook.com/")
# m_page_voice=100078451425619;xs=1%3AbJtdFsZmLHU9Mw%3A2%3A1702576445%3A-1%3A6399;wd=319x179;m_pixel_ratio=1;c_user=100078451425619;locale=en_GB;datr=KkF7ZfUmpcpj5IgiR6Rmvcdo;fr=0nK4bTXun8DmPjthk.AWV1pmtlMjNKmFP8qeedFPMqL7Q.Ble0El.O_.AAA.0.0.Ble0E8.AWVTBqoP-Co;sb=JUF7ZUMfqYcdrzJZmrSbdfpC;

# driver.add_cookie({"m_page_voice":"100078451425619","xs":"1%3AbJtdFsZmLHU9Mw%3A2%3A1702576445%3A-1%3A6399;wd=319x179","m_pixel_ratio":"1","c_user":"100078451425619","locale":"en_GB","datr":"KkF7ZfUmpcpj5IgiR6Rmvcdo","fr":"0nK4bTXun8DmPjthk.AWV1pmtlMjNKmFP8qeedFPMqL7Q.Ble0El.O_.AAA.0.0.Ble0E8.AWVTBqoP-Co","sb":"JUF7ZUMfqYcdrzJZmrSbdfpC",
# })
# for data in find_e:
#     data.click()
#     # find_d = driver.find_element(By.XPATH,"//*[@id='mount_0_0_No']/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/span")
#     # s = find_d.text
#     print(data)
sleep(1000)
driver.close()
# import os
# print(os.getcwd())

# import random
# from unidecode import unidecode
# with open("content.txt","r",encoding="utf-8") as r_content:
#     read = r_content.read()
#     list_r = read.split("\n")
#     print(list_r)
# # content = 

# print(random.choice(list_r))

