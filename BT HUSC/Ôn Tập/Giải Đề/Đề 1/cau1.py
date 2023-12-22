def string_e(value):
    str_r = ""
    for i in reversed(value):
        if i == " ":
            break
        else:
            str_r += i
    str_n = ""
    for i in reversed(str_r):
        str_n += i
        
    return str_n
        
list_name = []
while True:
    str_n = str(input())
    if str_n == "":
        break
    else:
        list_name.append(str_n)

cnt = 0
for i in list_name:
    if string_e(i) == "Anh":
        cnt += 1

print("So luong sinh vien co ten [Anh] : {}".format(cnt))

    

