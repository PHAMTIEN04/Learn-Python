import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dữ liệu
data = [73, 13, 85, 66, 23, 15, 1, 37, 38, 84, 15,48,78,10,41,67,2,78,13,68,62,2,39,3,85,33,35,32,1,99,24]
# Tạo các mẫu học máy
def create_dataset(data, look_back=3):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i + look_back])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

look_back = 3
X, y = create_dataset(data, look_back)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Dự đoán số tiếp theo
def predict_next_number(model, data, look_back):
    data = np.array(data[-look_back:]).reshape(1, -1)
    return model.predict(data)[0]

next_number = predict_next_number(model, data, look_back)
print(f"Số tiếp theo dự đoán: {next_number:.2f}")
