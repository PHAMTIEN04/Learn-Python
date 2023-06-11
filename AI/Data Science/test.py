import numpy as np
import matplotlib.pyplot as plt
# while True:
#     i = np.random.randint(1,100)
#     rng = np.random.RandomState(i)
#     x = rng.randn(100)
#     y = rng.randn(100)
#     colors = rng.randn(100)
#     sizes = 1000* rng.randn(100)
#     plt.scatter(x,y,c = colors,s = sizes,cmap="viridis",alpha= 0.3);
    
#     plt.show()

# e = ["I","Love","You"]
# v = ["Tôi","Yêu","Bạn"]
# eng = np.array(e)
# vie = np.array(v)
# input_e = str(input())
# for i in range(len(eng)):
#     if input_e == eng[i] :
#         print(vie[i])
#         break


m = int(input())
for i in range(2,m + 1):
    h =1 
    h = h * i
    
print(h)