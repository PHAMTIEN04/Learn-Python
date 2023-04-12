# # Hạn chế của vòng lặp while
# # Bạn có thể sử dụng vòng lặp while để có thể duyệt một List, chuỗi hoặc là một Tuple. Và thậm chí là một iterator (một object không hỗ trợ indexing) khi biết được số phần tử mà iterator đó chứa.

# # Ví dụ: 

# length = 3
# iter_ = (x for x in range(length))
# c = 0
# while c < length:
#      print(next(iter_))
#      c += 1


# # Nếu bạn không biết trước được số phần tử mà iterator đó có thì cũng không sao. Python vẫn cho phép bạn làm được điều đó bằng try-block (Kteam sẽ giới thiệu ở một bài khác)

# # Ví dụ:

# iter_ = (x for x in range(3)) # giả sử ta không biết có 3 phần tử
# while 1: # 1 là một expression True
#     try:
#         print(next(iter_))
#     except StopIteration:
#         break


# # Nhưng “con trăn” Python không thích sự rườm rà. Xưa nay vốn được biết đến với danh hiệu one-liner* nên điều này không chấp nhận được.
# # Vậy nên Python có một một vòng lặp khác giúp làm chuyện này đơn giản và ngắn gọn hơn chính là vòng lặp for.

# # Chú thích One-liner: Nhiều thuật toán dài hàng chục dòng có thể được viết ngắn gọn trong Python chỉ bằng một dòng. Điều này khá phổ biến với nhiều ngôn ngữ scripting đặc biệt trong số đó là Python.

# # Cấu trúc vòng lặp for và cách hoạt động

# # Chúng ta sẽ cùng tìm hiểu phần cấu trúc trước:

# # for variable_1, variable_2, .. variable_n in sequence:

#     # for-block

# # Sequence ở đây là một iterable object (có thể là iterator hoặc là một dạng object cho phép sử dụng indexing hoặc thậm chí không phải hai kiểu trên).

# # Lưu ý: Nếu sequence là một iterator object thì việc dùng vòng lặp duyệt qua cũng sẽ tương tự như bạn sử dụng hàm next.

# # Ở cấu trúc vòng lặp này, bạn có thể for bao nhiêu biến theo sau cũng được. Nhưng phải đảm bảm một điều rằng, nếu bạn for với n biến thì mỗi phần tử trong sequence cũng phải bao gồm n (không lớn hơn hoặc nhỏ hơn) giá trị để unpacking (gỡ) đưa cho n biến của bạn.

# # Một ví dụ thực tế: Tiếp tục serial về Kter “bờ rào” – Tèo. Tèo dẫn hai người bạn gái mình đi ăn kem. Tới quán kem thì Tèo phải kêu 3 cây kem cho Tèo và hai cô ghệ. Nếu chỉ gọi hai cây thì có thể Tèo phải nhịn còn nếu kêu bốn cây thì lúc đó sẽ có thể có xung đột xảy ra giữa ba người để tranh giành xem ai sẽ ăn hai cây.

# # Giả sử bạn có một sequence gồm 2 phần tử, mỗi phần tử gồm 3 giá trị và một đoạn code xử lí như sau:


# for e1, e2, e3 in char:
#     print("Elements:", e1, e2, e3)

# # Elements: a b c
# # Elements: 1 2 3

# # Bạn đưa vào vòng for gồm 3 biến e1, e2, e3.

# # Bây giờ là nói về cách hoạt động của vòng lặp for này.

# # Bước 1: Vòng for sẽ bắt đầu bằng cách lấy giá trị đầu tiên của sequence.

# # Bước 2: Giá trị đầu tiên này có 3 giá trị. Bạn đưa vào 3 biến. Kiểm tra hợp lệ.

# # Bước 3: unpacking 3 giá trị này và lần lượt gán giá trị này cho ba biến e1, e2, e3.

# # Bước 4: Thực hiện nội dung for-block (trong ví dụ: là việc in ra cả 3 biến).

# # Bước 5: Lấy giá trị tiếp theo của sequence sau đó làm tương tự như Bước 2, 3, 4.

# # Bước 6: Lúc này, sequence đã hết giá trị. Kết thúc vòng lặp. Kết quả ở đầu ra sẽ là 2 dòng cuối ở ví dụ trên.

# # Sử dụng vòng lặp để xử lí các iterator và Dict



# # Lí thuyết là thế! Giờ chúng ta sẽ làm một vài ví dụ bằng cách bắt đầu với vấn đề lúc đầu:

# iter_ = (x for x in range(3))
# iter_ = (x for x in range(3))
# for value in iter_:
#      print('->', value)

# # -> 0
# # -> 1
# # -> 2
# # value # biến value gián tiếp được khai báo
# # 2
# # next(iter_) # hãy học cách tiếp kiệp. Đây là object chỉ dùng một lần.
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # StopIteration

# # Tiếp đến chúng ta sẽ dùng vòng lặp này để duyệt một Dict. Nếu như một số ngôn ngữ khác phải có một vòng lặp mới for-reach thì với Python lại không cần.

# # Trước tiên hãy ôn lại bài cũ. Bạn còn chớ phương thức items của lớp Dict chứ? (nếu không, bạn có thể tham khảo lại trong bài KIỂU DỮ LIỆU DICT TRONG PYTHON)

# howkteam = {'name': 'Kteam', 'kter': 69}
# howkteam.items()
# # dict_items([('name', 'Kteam'), ('kter', 69)])

# # Dict-items không phải là một iterator object. Cũng không phải là một object cho phép bạn indexing. Nhưng nó vẫn là một iterable, nên ta có thể dùng một constructor nào đó để biến đổi nó về một thứ dễ xem xét hơn. Chẳng hạn thế này.

# list_values = list(howkteam.items())
# list_values
# [('name', 'Kteam'), ('kter', 69)]
# list_values[0]
# ('name', 'Kteam')
# list_values[-1]
# ('kter', 69)

# # Từ đó, ta có thể dễ dàng suy ra cách để có thể có được một vòng lặp duyệt một Dict. Và đây là ví dụ:

# for key, value in howkteam.items():
#     print(key, '=>', value)

# # name => Kteam
# # kter => 69

# # Đối với vòng for duyệt qua Dict mà chỉ có một biến chạy, thì biến đó sẽ duyệt qua các key của Dict:

# # Ví dụ:

# d = {1: 'one', 2: 'two', 3: 'three'}
# for i in d:
#     print(i)


# # Câu lệnh break, continue
# # Những câu lệnh này có chức năng hoàn toàn tương tự như trong vòng lặp while.

# # Ví dụ về câu lệnh break trong vòng lặp for:

# s = 'How Kteam'
# for ch in s:
#     if ch == ' ':
#         break
#     else:
#         print(ch)


# # Ví dụ về câu lệnh continue trong vòng lặp for

# s = 'H o w K t e a m'
# for ch in s:
#     if ch == ' ':
#         continue
#     else:
#         print(ch)

# # H
# # o
# # w
# # K
# # t
# # e
# # a
# # m

# # Cấu trúc vòng lặp for-else và cách hoạt động
# # Cấu trúc: 
# # for variable_1, variable_2, .. variable_n in sequence:

# #     # for-block

# # else:

# #     # else-block

# # Nếu bạn nắm rõ cách vòng lặp while-else hoạt động thì bạn cũng có thể tự đoán được cách mà for-else làm việc.

# # Cũng sẽ tương tự như while-else, vòng lặp hoạt động bình thường. Khi vòng lặp kết thúc, khối else-block sẽ được thực hiện. Và đương nhiên nếu trong quá trình thực hiện for-block mà xuất hiện câu lệnh break thì vòng lặp sẽ kết thúc mà bỏ qua else-block.

# # For-else bình thường:
# for k in (1, 2, 3):
#     print(k)
# else:
#     print('Done!')

# # 1
# # 2
# # 3
# # Done!

# # For-else có break:
# for k in (1, 2, 3):
#     print(k)
#     if k % 2 == 0:
#         break
# else:
#     print('Done!')

# # 1
# # 2

# Đọc Thêm Chi Tiết Tại https://howkteam.vn/course/lap-trinh-python-co-ban/vong-lap-for-trong-python-phan-1-2596

# Bài Tập 1
# iter_ = (x for x in range(3))
# for value in iter_:
#     print(value)

# # Traceback (most recent call last):
# #   File "<stdin>", line 2, in <module>
# # NameError: name 'non_exist_variable' is not defined

# print(next(iter_)) # kết quả là gì?
# Kết quả của hàm next(iter_) sẽ là số 0, vì khi sử dụng vòng lặp for với iterator iter_ trước đó, toàn bộ các giá trị có trong iter_ đã được duyệt qua và in ra màn hình console. Vì vậy, khi gọi hàm next(iter_) sau đó, iterator iter_ còn lại duy nhất một giá trị chưa được truy xuất, đó là số 0.

# Lưu ý rằng nếu chúng ta gọi hàm next(iter_) thêm một lần nữa, kết quả sẽ là số 1, và cuối cùng là số StopIteration sẽ được raise ra do các giá trị trong iter_ đã được truy xuất hết.

# Bài Tập 2
# Sử dụng vòng lặp để tính tổng các số trong set sau đây

# set_ = {5, 8, 1, 9, 4}
# sum = 0
# for i in set_:
#     sum += i
    
# print(sum)
    













# a = list(map(int,input("Nhập List :")))

# # print(a)
# # for i in range (0,len(a)-1) :
# #     for j in range (i+1,len(a)) :
# #         if a[i] > a[j] :
# #             temp = a[i]
# #             a[i] = a[j]
# #             a[j] = temp

# # for i in range (0,len(a)):
# #     print(a[i] , end=" ")

# print(min(a))