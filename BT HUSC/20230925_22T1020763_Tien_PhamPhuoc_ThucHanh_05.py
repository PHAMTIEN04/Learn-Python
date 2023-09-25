## 5
cs = 0
def maxc(n):
    global cs
    max = n[0]
    for i in range(1,len(n)):
        if max < n[i]:
            max = n[i]
            cs = i + 1
    return max
             
list_n = []
i = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        list_n.append(n)
        
print(f"So lon nhat la {maxc(list_n)} xuat hien tai vi tri thu #{cs}.")

