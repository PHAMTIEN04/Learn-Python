n = int(input())
data = list(map(int, input().split()))

# Initialize the total product and the sum of elements
total_product = 0
sum_of_elements = 0

# Calculate the total product and sum of elements in a single pass
for num in data:
    total_product += num * sum_of_elements
    sum_of_elements += num

print(total_product)
