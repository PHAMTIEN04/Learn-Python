n = input("Nhap: ")
str_n = str(n)
i = len(str_n) - 1
g = ""
cnt = 0

while i >= 0:
    g = str_n[i] + g
    if cnt == 2 or cnt == 5 or cnt == 8 and i > 0:
        g = "." + g
    i -= 1
    cnt += 1

print(g + " VND")
