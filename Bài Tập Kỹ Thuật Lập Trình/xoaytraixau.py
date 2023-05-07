n = int(input())
s = input()

# Số vị trí cần xoay trái sẽ được đưa về trong khoảng [0, len(s))
n %= len(s)

# Xoay trái xâu bằng cách đảo ngược 2 phần tử con
# Trong đó, phần tử con đầu tiên có chỉ số từ 0 đến n - 1
# Và phần tử con thứ hai có chỉ số từ n đến len(s) - 1
rotated_s = s[n:] + s[:n]

print(rotated_s)
