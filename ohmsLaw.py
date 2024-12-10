# Let's find ohm's law including, complex number system

R = int(input("Enter value for resistance: "))
Xc = complex(input("Enter value for capacitance: "))
Xl = complex(input("Enter value for inductance: "))
#R = complex(R)         -> initially this line was included assuming both term should be complex number
#                       to perform calculation

Z = R + 1j*(Xl-Xc)
#Z = str(Z)             -> this line was included assuming, Z should be string to include in formatted
#                           string
print(f"The impedence is: {Z}")

V = int(input("Enter the value for voltage: "))

I = V/Z         # Calcualtion of Current

power_factor = Z.real/abs(Z)

print(f"The power factor is: {power_factor:.2f}")


