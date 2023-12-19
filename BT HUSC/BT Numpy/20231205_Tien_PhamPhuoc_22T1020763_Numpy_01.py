import numpy as np
import random
# //1
la = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(la)

# //2
la2 = [[True,True,True],
     [True,True,True],
     [True,True,True]]
arr2 = np.array(la2)

# //3
la = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(la)
for i in arr:
    if i % 2 != 0:
        print(i)

# //4 
la = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(la)
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] = -1

print(arr)

# //5
print(5)
la = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(la)
i = 6
if len(arr) % 2 == 0 and len(arr) / i == 2:    
    c = arr.reshape(2,i)
    print(c)
else:
    print("Loi")


# //6
L1 = [random.randint(1,10) for x in range(1,10)]
L2= [random.randint(1,10) for x in range(1,10)]
a = np.array(L1)
b = np.array(L2)
xc = np.hstack((a,b))
print(a)
print(b)
print(xc)

# //7
L1 = [random.randint(1,10) for x in range(1,10)]
L2= [random.randint(1,10) for x in range(1,10)]
a = np.array(L1)
b = np.array(L2)
list_r = []
for i in a:
    if i in b:
        list_r.append(i)

pct = np.array(list_r)
print(pct)

# //8
L1 = [random.randint(1,10) for x in range(1,10)]
L2= [random.randint(1,10) for x in range(1,10)]
a = np.array(L1)
b = np.array(L2)
list_r = []
for i in a:
    if i in b:
        list_r.append(i)
    
cs = []
for i in range(0,len(a)):
    if a[i] in list_r:
        cs.append(i)
a = np.delete(a,[x for x in cs])

print(a)

# //9
L1 = [random.randint(1,10) for x in range(1,10)]
L2= [random.randint(1,10) for x in range(1,10)]
a = np.array(L1)
b = np.array(L2)
cs = []
for i in range(len(a)):
    try:
        if a[i] == b[i]:
            cs.append(i)
    except:
        break
print(cs)

# //10
L1 = [random.randint(1,10) for x in range(1,10)]
L2= [random.randint(1,10) for x in range(1,10)]
a = np.array(L1)
b = np.array(L2)
value1 = 0
value2 = 5
if value1 < value2:    
    print(a[value1:value2])
