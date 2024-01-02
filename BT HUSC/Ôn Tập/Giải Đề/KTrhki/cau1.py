
# D = "Truong Dai hoc Khoa hoc Dai hoc Hue"
# list_d = D.split(" ")
# list_check = []
# list_cnt = []
# cnt = 0
# for i in range(0,len(list_d)):
#     if list_d[i] not in list_check:
#         list_check.append(list_d[i])
#         for j in range(0,len(list_d)):
#             if list_d[i] == list_d[j]:
#                 cnt = cnt + 1
#         pw = cnt/len(list_d)*100
#         print("P({}): {}%".format(list_d[i],pw),end=", ")
#         cnt = 0


def tinhXacSuat(chuoi):


    words = chuoi.lower().split()



    soLanXuatHien = {}

    TongTu = len(words)



    for i in words:

        soLanXuatHien[i] = soLanXuatHien.get(i, 0) + 1



    for w, SoLan in soLanXuatHien.items():

        sacXuat = (SoLan / TongTu) * 100

        print(f"{w.capitalize()} : {sacXuat:.2f}%")



chuoi = input("Nhập chuỗi: ")

tinhXacSuat(chuoi)

