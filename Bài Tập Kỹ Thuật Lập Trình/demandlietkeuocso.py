n = int(input())
cnt = 0
list_r = []
for i in range(1,n+1):
    if n % i == 0:
        cnt = cnt + 1
        list_r.append(i)
        
print(cnt)
for i in list_r:
    print(i,end=" ")