# 3


n = int(input())

i = 1
F = 1

if i <= n:
    F = F * i
else:
    print(F)

F = F * i
i = i + 1

if i <= n :
    F = F * i
else: 
    print(F)
    
print(F)