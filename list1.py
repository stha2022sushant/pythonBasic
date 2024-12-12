# Ordered, mutable
# Heterogenous-> can content elements of different datatypes
# Support Duplications

#Basic Syntax 
my_list = ["Name", 23, 5.8, True]

print(my_list)

# Types:
    # Empty, Pure(with like data types, mixed, nested)

# Accessing elements of list

    # Indexing -> starts with index 0

number_list = [20, 30, 40, 50, 60, 70]
print(number_list[0])       # Prints first element
print(number_list[-1])      # Prints last element

# Slicing 
    # Generally prints elements from begining to one down to the end

print(number_list[1:4])     # prints elements from position 1 to 3
print(number_list[:3])      # prints elements from 0th position to 2
print(number_list[::2])     # prints every second elements
