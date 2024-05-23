s = str(input())
list_kt = ['-', '_', ';', '.', ',', '/', '|']
# print(s.split(list_kt))
for i in list_kt:
    if i in s:
        c = s.split(i)
        if(len(c)==3):
            c[1] = c[1].replace(' ',"")
            c[2] = c[2].replace(' ',"")
        
            if(c[2].isdigit() and c[1].isdigit()):
                print((int(c[2]) - int(c[1])) * 1200)
                break