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
print(number_list[::2])     # prints first elements and  every second elements
print(number_list[::-2])    # prints last element and every second elements


# List can be modified with various ways as

number_list[1] = 15

print(number_list)

# Elements can be added by various method as:
        # append(), insert(), extend()

# Append, means adding element to the end of the list

number_list.append(65)      # adds elements to the end of list

print(number_list)          

# Insert, in specific position

number_list.insert(2,45)     # insert 45 to index 2
print(number_list)

number_list.extend([91, 95,1])  # helps to add multiple elements to the existing list

print(number_list)



# For Removing Elements from the list

            # remove(), pop(), del(), clear() can be used


number_list.remove(1)       # Removes First occurance of 1

print(number_list)

removed_element = number_list.pop(2)        # Removes element in second index
print(number_list)                          # If index wasn't provided, last element would be removed by default


# number_list.clear()        -> clears all the elements in list

