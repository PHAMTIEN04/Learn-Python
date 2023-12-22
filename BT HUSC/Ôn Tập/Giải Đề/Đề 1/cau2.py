
list_r = []
n = int(input())
for i in range(n):
    mahp = str(input())
    tenhp = str(input())
    sotc = int(input())
    list_r.append({"mahp":mahp,"tenhp":tenhp,"sotc":sotc})

for i in list_r:
    if i["mahp"][0:3] == "TIN":
        print(i)

str_c = str(input())
for i in list_r:
    if str_c in i["tenhp"]:
        print(i["tenhp"])
