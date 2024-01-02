import numpy

n = int(input())
graph_matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    graph_matrix.append(row)
    
    
graph_matrix = numpy.array(graph_matrix)

graph_matrix_t = graph_matrix.T
print(graph_matrix)
print(graph_matrix_t)
check = True
for i in range(len(graph_matrix)):
    for j in range(len(graph_matrix_t)):
        if graph_matrix[i][j] != graph_matrix_t[i][j]:
            check = False
            break
    if check == False:
        break
if check == True:
    print("Đồ Thị Có Hướng")
else:
    print("Đồ Thị Vô Hướng")