l = input().split()
m = int(l[0])
n = int(l[1])
ga = 2
cho = 4
s_ga = 0
s_cho = 0
check = False

if m > 0:
    for i in range(1, m+1):
        check_c = i * cho
        check_g = (m - i) * ga
        total_legs = check_c + check_g

        if total_legs == n:
            s_cho = i
            s_ga = m - i
            check = True
            break

    if check and s_ga > 0 and s_cho > 0:
        print("Ga = ", s_ga, sep="")
        print("Cho = ", s_cho, sep="")
    else:
        print(-1)
