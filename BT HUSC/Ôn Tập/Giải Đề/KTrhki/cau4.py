from cau3 import CongNhan

def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for item in data:
            file.write(','.join(str(value) for value in item) + '\n')

list_cn = []
list_mcn = []

while True:
    maCN = str(input("Nhập mã công nhân: "))
    if maCN == "":
        break
    hoTen = str(input("Nhập họ tên: "))
    Bac = int(input("Nhập bậc: "))
    songaylv = int(input("Nhập số ngày làm việc: "))
    
    ngayKyHD_input = input("Nhập ngày ký hợp đồng (dd/mm/yyyy): ").split("/")
    ngayKyHD = {"day": int(ngayKyHD_input[0]), "month": int(ngayKyHD_input[1]), "year": int(ngayKyHD_input[2])}
    
    while maCN in list_mcn:
        print("Mã công nhân đã tồn tại. Nhập lại.")
        maCN = str(input("Nhập mã công nhân: "))
    
    list_mcn.append(maCN)
    list_cn.append(CongNhan(maCN, hoTen, Bac, songaylv, ngayKyHD))

# Lọc và lưu thông tin công nhân bậc 1 vào file CNBac1.txt
bac1_data = [(cn.maCN, cn.hoTen, f"{cn.ngayKyHD['day']}/{cn.ngayKyHD['month']}/{cn.ngayKyHD['year']}", cn.songaylv, cn.TienLuong()) for cn in list_cn if cn.Bac == 1]
save_to_file("CNBac1.txt", bac1_data)

# Sắp xếp danh sách cán bộ theo thứ tự tăng dần của ngày ký hợp đồng
sorted_list_cn = sorted(list_cn, key=lambda x: (x.ngayKyHD['year'], x.ngayKyHD['month'], x.ngayKyHD['day']))

# Hiển thị thông tin cán bộ ra màn hình
print("\nThông tin các cán bộ sau khi sắp xếp:")
for cn in sorted_list_cn:
    print(f"Mã CN: {cn.maCN}, Họ tên: {cn.hoTen}, Ngày ký HĐ: {cn.ngayKyHD['day']}/{cn.ngayKyHD['month']}/{cn.ngayKyHD['year']}, Số ngày làm việc: {cn.songaylv}, Tiền lương: {cn.TienLuong()}")
