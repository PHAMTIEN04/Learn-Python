def gt(value):
    check = 1
    while value > 0:
        check = check * value
        value = value - 1

    return check
def c_du(value):
    check = list(str(value))
    cnt = 0
    check_t_f = False
    for i in range(len(check)):
        if check[i] == '.':
            check_t_f =True
        if check_t_f == True:
            cnt = cnt + 1
    return cnt
        
s = 1.0
x = float(input())
if abs(x) <= 30:
    epsilon = 1e-9 # Ngưỡng

    i = 1
    term = (x ** i) / gt(i)

    while term > epsilon:
        s = s + term
        i = i + 1
        term = (x ** i) / gt(i)
        print(term)


    print("{:.4f}".format(s))



