##1
def my_total(sentence):
    cnt_h = 0
    cnt_t = 0
    for i in sentence:
        if i >= 'a' and i <= 'z':
            cnt_t = cnt_t + 1
        if i >= 'A' and i <= 'Z':
            cnt_h = cnt_h + 1
    
    return "So luong ki tu thuong: {} \nSo luong ki tu hoa: {}".format(cnt_t,cnt_h)

##2 
def my_sum_rep(digit,N):
    i = 1
    sum = 0
    save = digit
    check=""
    while i <= N:
        check = check + str(save)
        sum = sum + int(check)  
        i = i + 1
    return sum

##3
def my_check(password):
    checka_z = False
    checkA_Z = False
    check_num = False
    check_kt = False
    check_len = False
    for i in password:
        if i >= 'a' and i <= 'z':
            checka_z = True
        if i >= 'A' and i <= 'Z':
            checkA_Z = True
        if i >= '0' and i <= '9':
            check_num = True
        if i == '@' or i == '#' or i == '$':
            check_kt = True
        if len(password) >= 8:
            check_len = True
    if checka_z == True and checkA_Z == True and check_num == True and check_kt == True and check_len == True:
        return True
    else:
        return False
        
##4
def my_students(info_str):
    cnt = 1
    cnt_kt = 0
    print(cnt," ",sep="",end="")
    for i in info_str:
        if i != ',' and i != " ":
            print(i,end="")
        elif i == ',':
            cnt_kt = cnt_kt + 1
            if cnt_kt == 1:
                print("\t",end="")
            elif cnt_kt == 2:
                print("  ",end="")
        elif i == " ":
            cnt = cnt + 1 
            cnt_kt = 0
            print()
            print(cnt," ",sep="",end="")
    return ""

##5
sum = 1
def my_fraction(n):
    global sum
    if n == 0:
        return ""
    sum = sum + 1/n
    my_fraction(n-1)
    return sum


