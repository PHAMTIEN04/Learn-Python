def length(list_str):
    cnt = 0
    for i in list_str:
        if i == ',':
            cnt = cnt + 1
    return cnt + 1
    
def total(list_str):
    
    str_t = ""
    list_r = []
    for i in list_str:
        if i >= '0' and i <= '9':
            str_t = str_t + i
        if i == ',' or i == ']':
            list_r.append(str_t)
            str_t = "" 
    sum = 0
    for i in list_r:
        if i != '':
            sum = sum + int(i)

    return sum


def contains(list_str,item):
    str_t = ""
    list_r = []
    for i in list_str:
        if i != ','and i != '[' and i != ']':
            str_t = str_t + i
        if i == ',' or i == ']':
            list_r.append(str_t)
            str_t = ""
    check = " "+ str(item)
    if check in list_r:
        return True
    else:
        return False
    
def find_item(list_str,item):
    str_t = ""
    list_r = []
    for i in list_str:
        if i != ','and i != '[' and i != ']':
            str_t = str_t + i
        if i == ',' or i == ']':
            list_r.append(str_t)
            str_t = ""
    check = False
    str_n = " " + str(item)
    for i in range(len(list_r)):
        if str_n == list_r[i]:
            check = True
            loc = i

    if check == True:
        return loc
    else:
        return -1


def count_item(list_str,item):
    str_t = ""
    list_r = []
    for i in list_str:
        if i != ','and i != '[' and i != ']':
            str_t = str_t + i
        if i == ',' or i == ']':
            list_r.append(str_t)
            str_t = ""
    cnt = 0
    str_n = " " + str(item)
    for i in range(len(list_r)):
        if str_n == list_r[i]:
            cnt = cnt + 1
            
    return cnt
def reduce(IPv4_address):
    str_n = ""
    for i in range(len(IPv4_address)):
        if IPv4_address[i] != '0':
            str_n = str_n + IPv4_address[i]
        
    return str_n

def filter_number(str_c):
    i = 0
    str_n = ""
    list_n = []
    cnt = 0
    while i <= len(str_c)-2:
        # print(str_c[i])
        j = i + 1
        if str_c[i].isdigit() and not(str_c[j].isdigit()):
            str_n = str_n + str_c[i]
            list_n.append(str_n)
            str_n = ""
        elif str_c[i].isdigit() and str_c[j].isdigit():
            str_n = str_n + str_c[i] + str_c[j]
    
            i = j
            try:
                while str_c[j+1].isdigit():
                    j = j + 1
                    str_n = str_n + str_c[j]
                    i = j
            except:
                i = i - 1
            list_n.append(str_n)
            str_n = ""
    
        i = i + 1

    if str_c[i].isdigit() and not(str_c[i-1].isdigit()):
        str_n = str_n + str_c[i]
        list_n.append(str_n)
        str_n = ""

    print(list_n)
    
    str_nn = '"' + "["
    for i in range(len(list_n)):
        if i != len(list_n)-1:
            str_nn = str_nn + list_n[i] + ", "

        else:
            str_nn = str_nn + list_n[i] + "]" + '"'

    return str_nn

def split_quotation(str_c):        
    str_n = ""
    list_str = list(str_c)
    list_n = []
    check = False
    cnt = 0
    for i in range(len(list_str)):
        if check == True:
            if list_str[i] != '"':
                str_n = str_n + list_str[i] 
        if list_str[i] == '"':
            check = True
            cnt = cnt + 1
        
        if cnt == 2:
            list_n.append(str_n)
            check = False
            str_n = str_n + " "
            cnt = 0

    return str_n