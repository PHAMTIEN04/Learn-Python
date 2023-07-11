import openpyxl
import os
import calendar
import datetime 
os.chdir(r"D:/Learn Python/Project/Diem Danh Excel")

filename = "diemdanh.xlsx"

def tickexecl(filename, paper_sheet, row_col, value):
    workbook = openpyxl.load_workbook(filename=filename)
    sheet = workbook[paper_sheet]
    sheet[row_col].value = value
    workbook.close()
    workbook.save(filename=filename)

worbook1 = openpyxl.load_workbook(filename=filename)
sheet1 = worbook1["Trang_tính1"]
list_sv = ["Phạm Phước Tiến","Lê Vũ Trang","Nguyễn Thanh An"]
check  = int(sheet1["A1"].value)
worbook1.close()
worbook1.save(filename=filename)
cnt = 2
alpha = "A"
if check < 6:
    run_check = ord(alpha)
    run_check = run_check + check
    alpha = chr(run_check)
    check_t = False
    while cnt < len(list_sv)+2 :
        check_t = True
        tickexecl(filename=filename,paper_sheet="Trang_tính1",row_col=alpha + str(cnt),value="✓")
        cnt = cnt+1    

    worbook2 = openpyxl.load_workbook(filename=filename)
    sheet2 = worbook2["Trang_tính1"]
    sheet2["A1"].value = check + 1
    worbook2.close()
    worbook2.save(filename=filename)