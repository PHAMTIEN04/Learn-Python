# Các phương thức tiện ích

# Phương thức copy
# Cú pháp: <Dict>.copy()
# Công dụng: Giống với phương thức copy trong LIST. Để làm gì thì chắc các bạn cũng có thể suy nghĩ ra.

# Ví dụ 
d = {"Team" : "Kteam", (1,2) : 69}
d_copy   = d.copy()
print(d)
print(d_copy)

# Phương thức clear
# Cú pháp: <Dict>.clear()
# Công Dụng : Loại bỏ tất cả những phần tử có trong Dict

# Ví dụ :

d_clear_text ={"text1" : "xoa sach"}
d_clear_text.clear()
print(d_clear_text)


# Các phương thức xử lí

# Phương thức get
# Cú pháp: <Dict>.get(key [,default])
# Công dụng: Trả về giá trị của khóa key. Nếu key không có trong Dict thì trả về giá trị default. Default có giá trị mặc định là None nếu chúng ta không truyền vào.

# Ví dụ :

d_get_text = {"Textget" : "value"}
d_get = d_get_text.get("Textget","Baby")
print(d_get)

# Phương thức items
# Cú Pháp :  <Dict>.items()
# Công dụng: Trả về một giá trị thuộc lớp dict_items. Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.
# Dict_items là một iterable.

# Ví dụ : 

d_items_text = {"Textitems " : "valueitems",(1,2) : 69}
d_items = d_items_text.items()
print(d_items)

# Phương thức keys
# Cú pháp: <Dict>.keys()
# Công Dụng : Trả về một giá trị thuộc lớp dict_keys. Các giá trị của dict_keys sẽ là các key trong Dict.

# Ví dụ :

d_keys_text = {"Textkeys" : "Valuekeys"}
d_keys = d_keys_text.keys()
print(d_keys)

# Phương thức values
# Cú pháp: <Dict>.values()
# Công dụng: Trả về một giá trị thuộc lớp dict_values. Các giá trị của dict_values sẽ là các value trong Dict.
# Dict_values là một iterable.

# Ví dụ :

d_values_text = {"Textvalues" : "Values"}
d_values = d_values_text.values()
print(d_values)

# Phương thức pop
# Cú pháp: <Dict>.pop(key [,default])
# Công dụng: Bỏ đi phần tử có key và trả về value của key đó. Trường hợp key không có trong dict.
# Báo lỗi KeyError nếu default là None (ta không thêm vào).
# Trả về default nếu ta thêm default vào.

# Ví dụ 

d_pop_text = {"Textpop" : "Valuespop"}
d_pop = d_pop_text.pop("Textpop","NOne nha")
print(d_pop)
print(d_pop_text)

# Phương thức popitem
# Cú pháp: <Dict>.popitem()
# Công dụng: Trả về một 2-tuple với key và value tương ứng bất kì (vấn đề này liên quan đến giá trị của hash của key. Do đó bạn cũng hiểu vì sao key buộc phải là một hash object) trong Dict.
# Và cặp key-value sẽ bị loại bỏ ra khỏi Dict.

# Nếu Dict là một empty Dict. Sẽ có lỗi KeyError

# Ví dụ : 

d_popitem_text = {"Textpopitem" : "Valuepopitem",(1,2) : 69}
d_pop = d_popitem_text.popitem()
print(d_pop)
print(d_popitem_text)

# Phương thức setdefault
# Cú pháp: <Dict>.setdefault(key [,default])
# Công dụng: Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default. Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.
# Default mặc định là None

# Ví dụ : 

d_setdefault_text = {"textsetdefault" :"valuesetdefault"}
d_setdefault = d_setdefault_text.setdefault("texx","deptrai")
print(d_setdefault)
print(d_setdefault_text)

# Phương thức update
# Cú pháp: <D>.update([E, ]**F) 
# Công dụng: Phương thức giúp bạn cập nhật nội dung cho Dict.
# F là một Dict được tạo thành bởi packing arguments (khái niệm sẽ được Kteam giải thích ở một bài trong tương lai). Và sẽ thêm vào Dict bằng cách:

# Ví dụ : 

d_update_text = {"Textupdate " : "Valueupdate"}
d_update = d_update_text.update(Textupdate = "aaa",c=2)
print(d_update)
print(d_update_text)

# Toán tử “|” với 2 dict
# Cú pháp : <Dict_A> | <Dict_B>
# Công dụng: Trả về một dict mới với các cặp key – value có mặt ở một trong 2 dict. Nếu một key bất kì có trong cả 2 dict, thì giá trị được lấy sẽ là cặp key – value ở Dict_B

dict_a = {"1" : "2" , "3": "5"}
dict_b = {"1" : "3" , "32":"40"}
dict_check = dict_a | dict_b
print(dict_check)

# Câu hỏi củng cố
# 1. Tại sao thay đổi  dict2 mà dict1 lại cũng bị thay đổi theo? Hãy cho  giải pháp khắc phục
# = > Tại vì dict2 = dict1 thì cả 2 đang trỏ vào một vùng nhớ 
# = > Ta có thể sử dụng phương thức Copy để khác phục 
# 2. Nêu sự khác nhau giữa 
# d = {}
# print(d.update( {3}))
# print(d)
# Lỗi ở đoạn code trên do phương thức update() yêu cầu đối số phải là một dictionary. Trong trường hợp này, {3} chỉ là một set với một phần tử và không phải là một dictionary.
# d = {}
# print(d.update({3 : "Tien"}))
# Đoạn này có đẩy đủ Key và Value là một dictionary