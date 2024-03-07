x = [-2,0,2]
p_x = [2,3,4]
p_x1 = [4,5,6]
size = len(p_x) + len(p_x1)
x_new = []
p_new = []
# print(size)
check = 0
for i in range(1,size+1):
    x_new.append(x[check])
    p_new.append(p_x[check])
    if(i%2==0): check+=1
print(x_new)
print(p_new)
c_len = len(p_new)
i = 0
j = 1
k = 0
cnt = 0
arr_c = []
while True:
    if(p_new[j] - p_new[i] == 0):
        value = p_x1[cnt]
        cnt+=1
    else:
        value = (p_new[j] - p_new[i])/(x_new[j+k] - x_new[i])
    arr_c.append(value)
    
    if j+1 == len(p_new):
        p_new = arr_c
        arr_c = []
        i = -1
        j = 0
        k += 1
        print(p_new)
    if len(p_new) == 1: 
        break
    i+=1
    j+=1
        