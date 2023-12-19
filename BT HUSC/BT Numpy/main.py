import numpy as np

#1
arr = np.arange(0,10)
print(arr)
#2
arr = np.full((3,3),True)
print(arr)
#3
arr = np.arange(0,10)
print(arr[arr%2!= 0])
#4
arrc = np.arange(0,10)
arr = arrc[arr%2!= 0]
for i in range(len(arrc)):
    if arrc[i] in arr:
        arrc[i] = -1
print(arrc)
#5
la = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(la)
i = 5
if len(arr) % 2 == 0 and len(arr) / i == 2:    
    c = arr.reshape(2,i)
    print(c)
else:
    print("Loi")  
#6
a = np.arange(0,10)
b = np.arange(0,10)
m = np.hstack((a,b))
print(m)
#7
a = np.arange(0,10)
b = np.arange(0,10)
m = np.intersect1d(a,b)
print(m)
#8
a = np.arange(0,10)
b = np.arange(0,5)
cs = []
for x in range(len(a)):
    if a[x] in b:
        cs.append(x)
a = np.delete(a,cs)        
print(a)
#9
a = np.arange(0,10)
b = np.arange(0,5)
cs =[]
for i in range(len(a)):
    try:
        if a[i] == b[i]:
            cs.append(i)
    except:
        break
print(cs)
#10
a = np.arange(0,10)
value1 = 0
value2 = 100
if value1 < value2:
    for i in a:
        if i >= value1 and i <= value2:
            print(i)