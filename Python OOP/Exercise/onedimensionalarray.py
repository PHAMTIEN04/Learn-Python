
class one_dimensional_array:
    def __init__(self,size):
        self.a = []
        self.size = size
    def input(self):
        input_str = input()
        values = input_str.split(" ")
        for i in range(0,self.size):
            self.a.append(int(values[i]))
    def output(self):
        for i in range(0,self.size):
            print(self.a[i],end=" ")
            
arr = one_dimensional_array(5)
arr.input()
arr.output()