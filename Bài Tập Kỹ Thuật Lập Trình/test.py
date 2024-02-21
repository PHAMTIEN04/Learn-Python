import random

a = [1,2,3,5,7]


while True:
    b = random.choices(a,k=3)
    check = True
    for i in range(1,len(b)):
        if b[0] == b[i]:
            check= False
            break
    if check == True: 
        check = str(b[0]) + str(b[1]) + str(b[2])
        oke1 = random.choice(a)
        oke2 = random.choices(a,k=2)
        check1 = int(oke1)
        check2 = str(oke2[0]) + str(oke2[1]) 
        check3 = int(oke2[0]) + int(oke2[1])
        if oke1 not in b and oke2 not in b:
            if int(check) + check1 == 130 :
                print("{} + {} = 130".format(check,check1))
                break
            if int(check) + int(check2) == 130 :
                print("{} + {} = 130".format(check,check2))
                break
            if int(check) + check3 == 130 :
                print("{} + {} = 130".format(check,check3))
                break