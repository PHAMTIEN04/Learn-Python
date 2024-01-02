import numpy
n = int(input())
g_m = []
for i in range(n):
    row = list(map(int,input().split()))
    g_m.append(row)

g_m = numpy.array(g_m)

g_m_t = g_m.T
check = True
for i in range(len(g_m)):
    for j in range(len(g_m)):
        if g_m[i][j] != g_m_t[i][j]:
            check =False
            break
    if check == False:
        break
    
if check == True:
    print("Đồ Thị Có Hướng")
else:
    print("Đồ Thị Vô Hướng")