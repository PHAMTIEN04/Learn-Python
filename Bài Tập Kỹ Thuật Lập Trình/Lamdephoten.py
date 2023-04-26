def xoakitu(a, k):
    a = a[:k] + a[k+1:]
    return a

a = str(" Hello     World")
while a[0] == ' ':
    a = xoakitu(a, 0)
while a[-1] == ' ':
    a = xoakitu(a, -1)
for i in range(len(a)-1):
    if a[i] == ' ' and a[i+1] == ' ':
        a = xoakitu(a, i)
        i -= 1

print(a)
