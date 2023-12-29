m = int(input())
n = int(input())


def ntcn(m,n):
    um = []
    un = []
    for i in range(1,m+1):
        if m%i == 0:
            um.append(i)
    for i in range(1,n+1):
        if n%i == 0:
            un.append(i)
        
    print(um)
    print(un)
    usc = []

    for i in um:
        if i in un:
            usc.append(i)
    print(usc)
    if len(usc) > 1 :
        print("{} va {} khong phai so nguyen to cung nhau".format(m,n))
    elif len(usc) == 1:
        print("{} va {} la so nguyen to cung nhau".format(m,n))

ntcn(m,n)