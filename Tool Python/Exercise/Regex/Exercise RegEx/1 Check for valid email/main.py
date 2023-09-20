import re
## *Method 1
i_mail = input("Input Email: ")
# cut_text = re.compile(r"(.*?)")
check_mail_kt = re.compile(r"\@|\.")
check_mail_kt = check_mail_kt.findall(i_mail)
# print(len(check_mail_kt))
check = re.compile(r"(.*?)@(.*?)\.(.*)")
check = check.findall(i_mail)
# print(check)
if len(check_mail_kt) != 0:
    if   len(check_mail_kt) == 2 and(check_mail_kt[0] == '@' and check_mail_kt[1] == '.'):
        kt_text = check[0][0]
        kt_one = check[0][1]
        kt_two = check[0][2]
        if kt_one == "example" and kt_two == "com":
            print("Email Confirm!!!")
        else:
            print("Email Error!!!")
        # print("Text: ",kt_text)
        # print("@: ",kt_one)
        # print(".: ",kt_two)
    else:
        print("Email Error!!!")
else:
    print("Email Error!!!")

# print(check_mail_kt)
# print(i_mail)

## *Method 2
# i_mail = input("Input Email: ")
# email_pattern = r"^[a-zA-Z0-9._%+-]+@example\.com$"

# if re.match(email_pattern, i_mail):
#     print("Email Confirm!!!")
# else:
#     print("Email Error!!!")