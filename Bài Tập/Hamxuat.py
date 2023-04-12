# Vì sao cần hàm print
# Nếu bạn hay dùng interactive prompt thì bạn nhân ra rằng, kết quả luôn xuất hiện sau mỗi dòng code của bạn. Tuy nhiên, 
# nó sẽ không như vậy khi bạn viết những dòng code vào trong một file Python và chạy chương trình đó.

# Bạn cần một hàm giúp bạn xuất các nội dung mà bạn muốn cụ thể ở đây là xuất ra Shell (terminal, command prompt, powershell,…). 
# Đó là lí do hàm print ra đời!

# * Tìm hiểu cách sử dụng hàm print thông qua các parameter
# Hàm print có cú pháp như sau
# * Cú Pháp : print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Chúng ta sẽ tìm hiểu parameter đầu tiên

# *objects
# * chính là packing argument. Ở đây hiểu nôm na là nó gom lại các argument của bạn lại thành một Tuple
packing = 1,2,3,4
print(packing)
# Khi bạn truyền các argument vào hàm (giá trị 1, giá trị 2, giá trị 3,…) thì nó sẽ gói lại thành một Tuple giống như trên.
print("Kteam")
print("Kteam","Free Education")
print("Kteam" + str(69))
print("Kteam",69)
# Nhờ như vậy, bạn có thể truyền argument vào hàm print với số lượng bất kì. Điều này giúp bạn không phải ép kiểu dữ liệu, 
# để rồi nối chúng lại với nhau thành một giá trị rồi mới truyền cho hàm print.

# Để hiểu điều đó, chúng ta tới với parameter tiếp theo

# * sep (separate – chia ra, phân ra)
# Giá trị mặc định của parameter này là một khoảng trắng. Khi các argument bạn ném vào cho hàm print để hàm print in ra nội dung, 
# như đã biết là nó sẽ được gói vào một Tuple. Các giá trị trong Tuple sẽ được nối với nhau bằng parameter sep.

# Lưu ý: Khi truyền giá trị vào cho parameter theo cách keyword argument thì sẽ không bị packing. 
# Nghĩa là sẽ không bị gói vào trong giá trị của parameter object.
print("Kteam","Free","Educatiom",sep=", ")


# Tiếp theo là một parameter khá rắc rối

# end (kết thúc bằng)
# Đầu tiên, hãy chạy một file Python với nội dung sau đây.
print('line 1')
print('line 2')
print('line 3')

# Nếu bạn từng học qua ngôn ngữ lập trình C hoặc C++ hay là Java cũng có thể là C#. Bạn sẽ nhận thấy, mỗi lần print, chúng sẽ tự xuống dòng.

# Đó là nhờ parameter end. Nó sẽ tự thêm một kí tự newline (\n) vào cuối để có thể đưa con trỏ xuống dòng mới thay vì bạn phải tự thêm \n như một 
# số ngôn ngữ lập trình khác (một số ngôn ngữ lập trình có hỗ trợ thêm phương thức giúp xuất nội dung và tự động xuống dòng)

# Và đương nhiên, chúng ta cũng có thể thay đổi giá trị của parameter này.


print("how kteam",end=" ")
print("Education")
print("how kteam",end="|||")
print("Education")







from time import sleep # nhập hàm sleep từ thư viện time

print("Start")

cham = "....."
for c in cham :
    print(c,end="")
    sleep(0.5)
print("\nEnd")


print("start",end=" ") 

sleep(3)
print("end")

# Mặc định hàm print sẽ ghi nội dung vào file sys.stdout. Cũng nhờ vậy, bạn mới thấy được nội dung trên shell. 
# Đương nhiên, dựa vào đây, ta cũng có thể sử dụng hàm print như là phương thức write trong việc ghi file.
with open("filetext.txt", "w") as f :
    print("Tien oi ban dep trai qua", file=f)
    
with open("filetext.txt", "r") as f :
    print(f.read())


# Một đoạn code nhỏ dành cho bạn tự nhiên cứu:

your_name = "Henry"
your_great = "Hello! My Name Is " 
for c in your_great + your_name :
    print(c,end="")
    sleep(0.1)