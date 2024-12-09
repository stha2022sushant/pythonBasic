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
print("The substration of complex number is: " + complexSubstract)
print("The multiplication of complex number is: " + complexMultiplication)
print("The Division of complex number is: " + complexDivision)

# let's try some if/else condition
# to get only required value

#userInput = input("Enter 'A/a' for addition, 'B/b' for substration, 'C/c' for Multiplication, 'D/d' for division")

userInput = input("""\n Enter 'A/a' for addition,
'B/b' for subtraction,
'C/c' for multiplication,
'D/d' for division : """)

if(userInput == 'a'):
    print(complexAddition)
elif(userInput == 'b'):
    print(complexSubstract)

elif(userInput == 'c'):
    print(complexMultiplication)
elif(userInput == 'd'):
    print(complexDivision)
else:
    print("Invalid Input")
