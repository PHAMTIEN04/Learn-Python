s = str(input())

# Khởi tạo một dictionary để lưu số lần xuất hiện của từng ký tự
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Duyệt qua từng ký tự của chuỗi ban đầu
for c in s:
    # Nếu ký tự đó là một trong 4 ký tự A, C, G, T
    if c in count:
        count[c] += 1

# Tìm ký tự xuất hiện nhiều nhất và số lần xuất hiện của nó
max_count = max(count.values())

# In ra kết quả
print(max_count)