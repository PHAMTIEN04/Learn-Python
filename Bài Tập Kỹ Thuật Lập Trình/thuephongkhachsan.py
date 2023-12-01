list_r = input().split(" ")
n = int(list_r[0])
m = int(list_r[1])
k = int(list_r[2])

if n >= 0 and m <= 100 and (k >= 1 and k <= 100):
    tinhn = n / k
    tinhn2 = n // k
    checkn = 0
    if(tinhn != tinhn2):
        checkn = tinhn2 + 1
    else:
        checkn = tinhn2
    tinhm = m / k
    tinhm2 = m // k
    checkm = 0
    if(tinhm != tinhm2):
        checkm = tinhm2 + 1
    else:
        checkm = tinhm2
    sum = checkn + checkm
    print(sum)