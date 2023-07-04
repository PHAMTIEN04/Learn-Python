class two_dimensional_array:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.a = []

    def input(self):
        for i in range(self.m):
            input_str = input()
            row_values = input_str.split()
            row = [int(value) for value in row_values]
            self.a.append(row)

    def output(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.a[i][j], end=" ")
            print("\n", end="")

arr = two_dimensional_array(3, 4)
arr.input()
arr.output()
