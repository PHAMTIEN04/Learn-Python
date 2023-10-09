## 4
def sumc(n):
    sum = 0
    if n < 0:
        n = -n
    while n != 0:
        check = n % 10
        if check % 2 == 0:
            sum = sum + check
        n = n // 10
    return sum
n = int(input())

print(f"Tong cac chu so chan trong {n} la",sumc(n))