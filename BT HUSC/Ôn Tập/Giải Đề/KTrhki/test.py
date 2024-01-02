n = int(input())
graph_matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    graph_matrix.append(row)
    
print(graph_matrix)