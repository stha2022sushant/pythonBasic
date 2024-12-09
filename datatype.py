# There are various type of datatype
#Numric:
    # 1. Integer Type: easy
    # 2. Float Type: easy
    # 3. Complex Number

# Let's make a simple calculating machine for complex number

complexNum1 = complex(input("Enter First Complex Num: "))
complexNum2 = complex(input("Enter Second Complex Num: "))

print(complexNum1)
print(complexNum2)

complexAddition = complexNum1 + complexNum2
complexSubstract = complexNum1 - complexNum2
complexMultiplication = complexNum1 * complexNum2
complexDivision = complexNum1 / complexNum2

complexAddition = str(complexAddition)
complexSubstract = str(complexSubstract)
complexMultiplication = str(complexMultiplication)
complexDivision = str(complexDivision)

print("The addition of complex number is: " + complexAddition)