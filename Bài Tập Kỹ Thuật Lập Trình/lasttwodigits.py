# Accept user input as a space-separated string and split it into a list
input_data = (input().split())

# Convert the input values to integers and assign them to variables a, b, c, and d
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
d = int(input_data[3])

# Check if all four variables (a, b, c, and d) are greater than or equal to 2
# and less than or equal to 10^9 (1 billion)
if (a >= 2 and b >= 2 and c >= 2 and d >= 2) and (a <= 10**9 and b <= 10**9 and c <= 10**9 and d <= 10**9):
    # Calculate the product of the four integers and store it in the variable x
    x = a * b * c * d

    # Convert the product x to a string and store it as a list of characters in da
    da = list(str(x))

    # Extract the last two characters of the string representation of x and store it in lt
    lt = da[-2] + da[-1]

    # Print the last two characters of the product
    print(lt)
