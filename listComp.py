# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Output: [0, 4, 16, 36, 64]



# Using a for loop
for item in my_list:
    print(item)

# Using enumerate to get index and value
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")