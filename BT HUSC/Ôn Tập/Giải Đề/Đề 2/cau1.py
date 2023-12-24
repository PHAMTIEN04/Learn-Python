str_i = str(input())
str_n = ""
for i in str_i:
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        str_n += i
    # print(i)

print(str_n)