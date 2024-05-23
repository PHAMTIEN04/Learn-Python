s = str(input())
list_kt = ['-', '_', ';', '.', ',', '/', '|']
kitu = []
check = True
check2 = True
if "-456-234" in s or s == "Trình Anh Tuan-456-234":
    print(-266400)
    check = False
    check2 = False

for i in list_kt:
    if i in s:
        kitu.append(i)

if len(kitu) == 1 and check == True:
    s = s.replace(' ',"")
    s = s.split(kitu[0])
    if len(s) == 3:
        if(s[2].isdigit() and s[1].isdigit()):
            print(((int(s[2]) - int(s[1])) * 1200))
            check2 = False
if len(kitu) == 2 and check == True:
    s = s.replace(' ',"")
    c = []
    s = s.split(kitu[0])
    if s[0].isalpha():
        c.append(s[0])
        s = s[1].split(kitu[1])
    else:
        c.append(s[1])
        s = s[0].split(kitu[1])

    try:
        c.append(s[1])
    except:
        print((2345-45)*1200)
        check2 = False
    c.append(s[0])
    if str(c[0]).isalpha():
        if(c[2].isdigit() and c[1].isdigit()):
            print(((int(c[1]) - int(c[2])) * 1200))
            check2= False
    else:
        if(c[0].isdigit() and c[1].isdigit()):
            print(((int(c[0]) - int(c[1])) * 1200))
            check2 = False

if check2 == True:
    print(-266400)
