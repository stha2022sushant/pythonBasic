# addition , subtraction, multiplication, division, modulus 
# Prompt user to input two different numbers in a single line

num1, num2 = map(float, input("Enter two number: ").split(","))

addition = num1 + num2                  # gives the addition of two number
subtraction = num1 - num2               # gives subtraction
multiplication = num1*num2              # gives multiplication
division = num1//num2                   # gives floor division
reminder = num1 % num2                  # gives the reminder 
exponential = num1 ** num2              # exponential number

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Division: ", division)
print("Modulus: ", reminder)
print("Exponential: ", exponential)