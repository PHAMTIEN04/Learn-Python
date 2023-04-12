# # Cấu trúc vòng lặp while và cách hoạt động

# # Nào! Cùng ngó sơ cấu trúc, sau đó Kteam sẽ giải thích cho bạn cách mà nó hoạt động

# # while expression:

# #      # while-block

# # Lưu ý: Việc chia block như thế này cũng giống như khi bạn sử dụng câu lệnh if và đã được Kteam giới thiệu ở bài trước CẤU TRÚC RẼ NHÁNH.

# # Nó sẽ hoạt động ra sao?
# # Rất đơn giản! Việc đầu tiên, Python sẽ kiểm tra giá trị boolean của expression. Nếu là False, thì bỏ qua while-block và đến với câu lệnh tiếp theo. Ngược lại, sẽ thực hiện toàn bộ câu lệnh trong while-block. Sau khi thực hiện xong, quay ngược lại kiểm tra giá trị boolean của expression một lần nữa. Nếu False thì bỏ qua while-block, còn True thì tiếp tục thực hiện while-block. Và sau khi thực hiện xong while-block lại quay về kiểm tra giá trị boolean expression như những lần trước.

# # Ví dụ:

# k = 5

# while k > 0:
#     print('k =', k)
#     k -= 1
# # ...
# # k = 5
# # k = 4
# # k = 3
# # k = 2
# # k = 1
# # k # k bằng 0 nên > 0 là một boolean False, do đó vòng lặp đã kết thúc
# # 0



# # Sử dụng vòng lặp để xử lí chuỗi, list, tuple


# # Đây là những iterable cho phép ta truy xuất một giá trị bất kí trong nó bằng phương pháp indexing. Thế nên, ta có thể nhờ điều này kết hợp với vòng lặp để xử lí chúng.

# s = 'How Kteam'
# idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
# length = len(s) # lấy độ dài chuỗi làm mốc kết thúc
# while idx < length:
#     print(idx, 'stands for', s[idx])
#     idx += 1 # di chuyển index tới vị trí tiếp theo
# # 0 stands for H
# # 1 stands for o
# # 2 stands for w
# # 3 stands for
# # 4 stands for K
# # 5 stands for t
# # 6 stands for e
# # 7 stands for a
# # 8 stands for m
# # Đơn giản phải không nào. List và Tuple hoàn toàn tương tự.

# # Câu lệnh break và continue

# # Lưu ý: Hai câu lệnh này chỉ có thể dùng trong các vòng lặp

# # Câu lệnh break
# # Câu lệnh break dùng để kết thúc vòng lặp. Cứ nó nằm trong block của vòng lặp nào thì vòng lặp đó sẽ kết thúc khi chạy câu lệnh này.

# # Trong trường hợp vòng lặp a chứa vòng lặp b. Trong vòng lặp b chạy câu lệnh break thì chỉ vòng lặp b kết thúc, còn vòng lặp a thì không.

# # Ví dụ *:

# five_even_numbers = []
# k_number = 1
# while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
#         if k_number % 2 == 0: # nếu k_number là một số chẵn
#             five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
#         if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
#             break # thì kết thúc vòng lặp
#         k_number += 1
# # ...
# print(five_even_numbers)
# # [2, 4, 6, 8, 10]
# # k_number
# # 10

# # Câu lệnh continue
# # Câu lệnh này dùng để chạy tiếp vòng lặp. Giả sử một vòng lặp có cấu trúc như sau:

# # while expression:

# #     #while-block-1

# #     continue

# #     #while-block-2


# # Khi thực hiện xong while-block-1, câu lệnh continue sẽ tiếp tục vòng lặp, không quan tâm những câu lệnh ở dưới continue và như vậy nó đã bỏ qua while-block-2.

# # Ví dụ: 

# k_number = 1
# while k_number < 10:
#     if k_number % 2 == 0: # nếu k_number là số chẵn
#         k_number += 1  # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
#         continue
#     print(k_number, 'is odd number')
#     k_number += 1
# # ...
# # 1 is odd number
# # 3 is odd number
# # 5 is odd number
# # 7 is odd number
# # 9 is odd number


# # Câu lệnh pass
# # Về cơ bản, pass có thể được hiểu như là “không có gì”. Nó dường như chỉ được để cho có.

# while expression:

#  pass

# # Khi thực hiện các lệnh trong vòng lặp (và cả hàm) , nó sẽ xem lệnh pass này như là “vô hình”. Nhưng nó sẽ giúp tránh lỗi nếu như vòng lặp (hàm) của bạn không có bất kì một lệnh nào.

# # Ví dụ: 

# a = 3
# b = 4
# while a > 0:
#     a -= 1
#     pass
#     b += 1

# print(b)
# # 7
# # >>>
# # while a > 0:
# # ...
# #   File "<stdin>", line 2

# #     ^
# # IndentationError: expected an indented block after 'while' statement on line 1
# # >>> while a > 0:


# # Cấu trúc vòng lặp while-else và cách hoạt động
# # Ta sẽ xem cấu trúc trước:

# # while expression:

# #     # while-block

# # else:

# #     # else-block

# # Cấu trúc này gần tương tự như while bình thường. Thêm một điều, khi vòng vòng lặp while kết thúc thì khối lệnh else-block sẽ được thực hiện.

# # Ví dụ:

# while k < 3:
#     print('value of k is', k)
#     k += 1
# else:
#     print('k is not less than 3 anymore')
# # ...
# # value of k is 0
# # value of k is 1
# # value of k is 2
# # k is not less than 3 anymore
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10
# # 11
# # Trong trường hợp trong while-block chạy câu lệnh break thì vòng lặp while sẽ kết thúc và phần else-block cũng sẽ không được thực hiện.

# # >>> k = 0
# # >>> while k < 5:
# # ...     print('value of k is', k)
# # ...     k += 1
# # ...     if k > 3:
# # ...         print('k is greater than 3')
# # ...         break
# # ... else:
# # ...     print('k is not less than 5 anymore')
# # ...
# # value of k is 0
# # value of k is 1
# # value of k is 2
# # value of k is 3
# # k is greater than 3

# # Hiện tượng vòng lặp vô tận
# # Các bạn cần lưu ý là, đối với vòng lặp while, trong nhiều trường hợp, bạn có thể sẽ không biết trước số lần lặp, và có thể sẽ có nhiều lỗi không mong muốn. Điển hình nhất là vòng lặp vô tận:

# # >>> a = 5
# # >>> while a != 0:
# # ...     a -= 

# # Đoạn code trên sẽ chạy mãi mãi mà không bao giờ dừng lại. Lí do là vì giá trị của biến a sẽ không bao giờ bằng 0.

# # Đối với những người mới học, cần nắm bắt rõ cách hoạt động của vòng lặp while để tránh các lỗi không đáng có.

# # Đọc Thêm Chi Tiết Tại : https://howkteam.vn/course/lap-trinh-python-co-ban/vong-lap-while-trong-python-2595

# Bài Tập 1
# Viết lại một vòng lặp có chức năng tương tự ví dụ * nhưng không dùng câu lệnh break
# five_even_numbers = []
# k_number = 1
# while len(five_even_numbers) < 5: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
#         if k_number % 2 == 0: # nếu k_number là một số chẵn
#             five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
#         k_number += 1

# print(five_even_numbers)

# Bài Tập 2 
# Viết lại một vòng lặp có chức năng tương tự ví dụ * nhưng không dùng câu lệnh break
# Cho một file text tên draft.txt như sau:
# an so dfn Kteam odsa in fasfna Kteam mlfjier
# as dfasod nf ofn asdfer fsan dfoans ldnfad Kteam asdfna
# asdofn sdf pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf
# afdna Kteam adfoasdf ncxvo aern Kteam dfad
# 1
# 2
# 3
# 4
# Trong file này có một số chữ Kteam (Kteam sẽ không xuất hiện ở đầu dòng), và trước nó là một chữ ngẫu nhiên nào đó và nhiệm vụ của bạn là đổi chữ đó thành How. Nhớ là sử dụng vòng lặp.

# Sau khi đổi thành công, bạn lưu nội dung đó vào file tên kteam.txt.

# Đây là mẫu của kteam.txt:

# an so How Kteam odsa in How Kteam mlfjier
# as dfasod nf ofn asdfer fsan dfoans How Kteam asdfna
# asdofn sdf How Kteam dfaojf kteam How Kteam dfaodf
# How Kteam adfoasdf ncxvo How Kteam dfad
# sapxep = ''
# with open(file="draft.txt",mode="r+",encoding="utf8") as filetext_bt :
#     check = filetext_bt.readline().split()
#     while len(check) != 0 :
#         k = 1
#         while k < len(check):
#             if check[k] == "Kteam":
#                 check[k-1] = "How"
#                 string = " ".join(check)
#             k = k + 1
#         string = " ".join(check)
#         sapxep += string + "\n"
#         check = filetext_bt.readline().split()


# with open(file="kteam.txt",mode="w",encoding="utf8") as filecheck_bt :
#     filecheck_bt.write(sapxep)
            
# print(k)
# print(check)

# sep = " "       
# string = sep.join(check)

# print(string) 
# Bài Tập 3
# Sắp xếp một mảng số nguyên có dạng như sau:
# [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

# Lưu ý: là các số 11 là những số cố định không được thay đổi vị trí của nó.

# Sau khi sắp xếp lại mảng trên sẽ là:

# [0, 14, 11, 34, 35, 56, 11, 11, 65, 90, 11, 756]

#CACH 1
# list_int = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
# k = 0

# while k < len(list_int) - 1 :
#     j = k + 1
#     if list_int[k] != 11 :
#         while j < len(list_int) :
#             if list_int[j] != 11 :
#                 if list_int[k] > list_int[j] :
#                     temp = list_int[k]
#                     list_int[k] = list_int[j]
#                     list_int[j] = temp
#             j = j + 1
#     k = k + 1
    
    
    
#Cach 2   
# data = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
# vitri11 = [] # Vị trí số 11 trong chuỗi data
# k = 0

# ### Bước 1: Vòng lặp thêm thứ tự số 11 vào vitri11 ###
# while k < len(data):
# 	if data[k] == 11:
# 		vitri11.append(k) # Thêm k vào chuỗi vitri11
# 		print('Vị trí số 11 là:',k)
# 	else:
# 		print('Không phải số 11')
# 	k += 1
# print('Vị trí của số 11 trong chuỗi data là:', vitri11)

# ### Bước 2: Xóa hết 11 trong chuỗi, sắp xếp thứ tự từ bé đến lớn ###
# k = 0
# while k < len(vitri11):
# 	data.remove(11)
# 	k += 1
# data.sort()
# print('Sắp xếp chuỗi từ bé đến lớn (không có 11): ',data)

# ### Bước 3: Sắp xếp chuỗi hoàn chỉnh ###
# k = 0
# kdata = 0
# sortdata = [] # sortdata = Sắp xếp list đã bỏ 11, từ bé đến lớn
# while k < 12:
# 	if k in vitri11:
# 		sortdata += [11]
# 		print(sortdata)
# 	else:
# 		sortdata += [data[kdata]]
# 		kdata += 1
# 		print(sortdata)
# 	k += 1
# print('Kết quả bài tập:',sortdata)