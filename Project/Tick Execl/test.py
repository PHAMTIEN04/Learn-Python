# import openpyxl
# import os
# import calendar


# # print(is_leap)
# os.chdir(r"D:/Learn Python/Project/Tick Execl")

# filename = 'TickLearn.xlsx'


# def tickexecl(filename,paper_sheet,row_col,value):
#     workbook = openpyxl.load_workbook(filename=filename)
#     sheet = workbook[paper_sheet]
#     sheet[row_col].value = value 
#     workbook.close()
#     workbook.save(filename=filename)
    
# import datetime

# # Lấy ngày và giờ hiện tại
# now = datetime.datetime.now()
# print("Ngày và giờ hiện tại:", now)
# a = str(now).split("-")
# print(a)
# print(a[2])
# a[2] = a[2].split(" ")
# print(a)
# year = a[0]
# month = a[1]
# day = a[2][0]
# time = a[2][1]
# print("Year:",year)
# print("Month:",month)
# print("Day:",day)
# print("Time:",time)
# is_leap = calendar.isleap(int(year))
# while True:
#     if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
#         number_of_day = 31
#         break
#     elif month == "04" or month == "06" or month == "09" or month == "11" :
#         number_of_day = 30
#         break
#     elif is_leap == True:
#         number_of_day = 29
#         break
#     elif is_leap == False:
#         number_of_day = 28
#         break

# print(number_of_day)
a =  ord("B")
print(type(a))
d = chr(a)
print(type(d))