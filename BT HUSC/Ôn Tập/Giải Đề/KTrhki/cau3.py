class CongNhan:

    def __init__(self, maCN='', hoTen='', Bac=0, songaylv=0, ngayKyHD={"day": 0, "month": 0, "year": 0}):
        self.maCN = maCN
        self.hoTen = hoTen
        self.Bac = Bac
        self.songaylv = songaylv
        self.ngayKyHD = ngayKyHD
    def TienLuong(self):
        bacs = {1: 300000, 2: 350000, 3: 400000}

        TienCongNhat = bacs.get(self.Bac, 0)
        return self.songaylv * TienCongNhat
    def hienThi(self):
        print(f"Mã công nhân: {self.maCN}")
        print(f"Họ tên: {self.hoTen}")
        print(f"Bậc: {self.Bac}")
        print(f"Số ngày làm việc: {self.songaylv}")
        print(f"Tiền lương: {self.TienLuong()}")


    def __gt__(self, other):
        if self.ngayKyHD["year"] > other.ngayKyHD["year"]:
            return True
        elif self.ngayKyHD["year"] == other.ngayKyHD["year"]:
            if self.ngayKyHD["month"] > other.ngayKyHD["month"]:
                return True
            elif self.ngayKyHD["month"] == other.ngayKyHD["month"]:
                return self.ngayKyHD["day"] > other.ngayKyHD["day"]
        return False


# s = CongNhan("22T", "tien", 1, 10, {"day": 10, "month": 10, "year": 2004})
# s.hienThi()

# s1 = CongNhan("22T", "tien", 1, 10, {"day": 10, "month": 10, "year": 2005})
# s1.hienThi()

# if s > s1:
#     print("Yes")
# else:
#     print("No")
