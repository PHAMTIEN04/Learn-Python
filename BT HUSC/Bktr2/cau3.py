from cau2 import KHACHHANG
import csv
# kh = KHACHHANG()
# kh.nhap()
# with open("KhachHang.csv","a",newline="") as csv_kh:
#     csv_writer = csv.writer(csv_kh,delimiter=",")
#     csv_writer.writerow([kh.mkh,kh.ht,kh.dc,kh.csc,kh.csm])
#     csv_kh.close()

list_kh = []
with open("KhachHang.csv","r") as csv_kh:
    csv_reader = csv.reader(csv_kh,delimiter=",")
    for line in csv_reader:
        list_kh.append(KHACHHANG(str(line[0]),str(line[1]),str(line[2]),int(line[3]),int(line[4])))
    csv_kh.close()

# for data in list_kh:
#     # data.hienthi()
#     if data.sld() > 50:
#         with open("KH50.csv","a",newline="") as kh50_csv:
#             kh50_writer = csv.writer(kh50_csv,delimiter=",")
#             kh50_writer.writerow([data.mkh,data.ht,data.dc,data.csc,data.csm])
#             kh50_csv.close()

max = list_kh[0].ttd()
for data in range(1,len(list_kh)):
    if max < list_kh[data].ttd():
        max = list_kh[data].ttd()
        
for data in list_kh:
    if data.ttd() == max:
        data.hienthi()
        print("Tien Dien Su Dung:",round(data.ttd(),3),"VND")
