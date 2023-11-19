n = int(input())
list_a = []
for i in range(1,n+1):
    if n % i == 0:
        list_a.append(i)

print(list_a)
check = False
for i in list_a:
    if i % 2 == 1:
        check = True
        
    else:
        check = False
        break

if check == True:
    print("yes")
else:
    print("No")