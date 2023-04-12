import bs4
import requests
import io
response=requests.get('http://nghiahsgs.com')
html_doc=response.text
#file=io.open('code.html',mode='w',encoding='utf8')
#file.write(html_doc)


soup = bs4.BeautifulSoup(html_doc, 'html.parser')
eles=soup.select('title')

for ele in eles:
	print(ele.get_text())
	#print(ele.get('href'))
 
 # Đoạn code trên sử dụng thư viện requests để gửi yêu cầu tới trang web http://nghiahsgs.com và lấy nội dung HTML của trang web đó. 
 # Sau đó, sử dụng BeautifulSoup để phân tích cú pháp HTML và trích xuất tiêu đề của trang web bằng cách sử dụng phương thức select 
 # của BeautifulSoup. Kết quả sẽ được in ra màn hình bằng cách sử dụng phương thức get_text của Tag object.
 
#  Cú pháp của thư viện BeautifulSoup trong Python như sau:

# Import thư viện:
# Code
# import bs4

# Tạo đối tượng BeautifulSoup từ nội dung HTML:
# code
# soup = bs4.BeautifulSoup(html_doc, 'html.parser')

# Sử dụng phương thức select để tìm các phần tử trong nội dung HTML dựa trên CSS Selector:
# code
# eles = soup.select('tag_selector')

# Sử dụng phương thức get_text() để lấy nội dung của một phần tử HTML:
# code
# ele.get_text()

# Trong đó:

# html_doc: là chuỗi HTML cần phân tích.
# tag_selector: là CSS Selector để lựa chọn phần tử.
# ele: là đối tượng phần tử HTML được chọn.