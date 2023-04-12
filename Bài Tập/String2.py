strA = "HowKteam.com\n"
strB = strA[0]
strC = strB in strA
print(strB )

#cắt chuỗi cú pháp : tên_biến[vị trí bắt đầu : vị trí kết thúc - 1]
#->Cắt từ trái sang phải
#len() : hàm kiểm kiểm tra độ dài của chuỗi
strCut = "HowKteam"
strCut1 = strCut[1:len(strCut)]
print(strCut1)

#Cú pháp cắt chuỗi từ phải sang trái : tên_biến[vị trí bắt đầu : vị trí kết thúc - 1 : bước nhảy ]
#dương thì từ trái sang phải còn âm thì từ phảo sang trái

strCut2 = "HowKteam"
strcut3 = strCut2[None:None:-1]
print(strcut3)


#Ép Kiểu Dữ Liệu : Kiểu_Dữ_Liệu(Giá Trị)
#Ép kiểu dữ liệu str thành int
a = int("69") + 5
#Ép Kiểu dữ liệu int thành str
b = str(69)+ "5"
print(a)
print(b)

#cú pháp thay đổi ki tự trong chuỗi
c = "HowKteam"
d = c[None:1] + "O" + c[2:None]
print(c)