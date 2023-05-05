# '''Cho dãy số 1,3,7,9,11,13...
# Nhập vào số nguyên N là độ dài dãy số
# In ra dãy số theo quy luật và tính tổng dãy số đó

# '''
N = int(input())
check = 100

str_test = []

cnt = 0
for i in range (0,check+1):
    if cnt < N:
        if i % 2== 1 and i % 5 != 0:
            str_test.append(i)
            cnt = cnt + 1
    else :
        break
    
print(str_test)
print(sum(str_test))