n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]

# Kiểm tra nếu giao điểm của hai đường chéo phụ là cùng một điểm
if n % 2 != 0:
    middle = n // 2
    sum2 -= a[middle][middle]

print(sum1 + sum2)

a = 1
print(type(a))