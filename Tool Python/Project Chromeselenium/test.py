import re 
import os

os.chdir(r"C:\Learn Python\Tool Python\Project Chromeselenium")
filename = 'account.txt'
lines = []

with open(file=filename, mode="r", encoding="utf8") as filetest:
    for line in filetest:
        lines.append(line.strip())  # loại bỏ kí tự xuống dòng
        


while True:
    i = 0
    regex_acc = re.compile(r"tk (.*?) :")
    kq_acc = regex_acc.search(lines[i])
    acc_fb = kq_acc.group(1)
    regex_pass = re.compile(r"mk (.*)")
    kq_pass = regex_pass.search(lines[i])
    pass_fb = kq_pass.group(1)
    print(acc_fb)
    print(pass_fb)
    i = i+1
    if i == len(lines):
        break