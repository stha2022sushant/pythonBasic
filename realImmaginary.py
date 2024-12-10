# this is to find real and immaginary part from complex number

complexNum = 3 + 5j
print(f"Real Part: {complexNum.real}")
print(f"Immaginary Part: {complexNum.imag}")



# Circuit parameters
R = 10                  # Resistance in ohms
X_L = 20                # Inductive Reactance in ohms
X_C = 5                 # Capacitive Reactance in ohms
V = 120                 # Voltage in volts (RMS)

# Step 1: Calculate Impedance (Z)
Z = R + 1j * (X_L - X_C)
print(f"Total Impedance (Z): {Z:.2f} ohms")

# Step 2: Calculate Current (I)
I = V / Z
print(f"Current (I): {I:.2f} A")

# Step 3: Calculate Power Factor (cos φ)
power_factor = Z.real / abs(Z)
print(f"Power Factor (cos φ): {power_factor:.2f}")

# Step 4 (Optional): Calculate Phase Angle
phase_angle = cmath.phase(Z)  # In radians
phase_angle_deg = phase_angle * (180 / cmath.pi)  # Convert to degrees
print(f"Phase Angle: {phase_angle_deg:.2f}°")




import cmath

# Circuit parameters
R = 10                  # Resistance in ohms
X_L = 20                # Inductive Reactance in ohms
X_C = 5                 # Capacitive Reactance in ohms
V = 120                 # Voltage in volts (RMS)

# Step 1: Calculate Impedance (Z)
Z = R + 1j * (X_L - X_C)
print(f"Total Impedance (Z): {Z:.2f} ohms")

# Step 2: Calculate Current (I)
I = V / Z
print(f"Current (I): {I:.2f} A")

# Step 3: Calculate Power Factor (cos φ)
power_factor = Z.real / abs(Z)
print(f"Power Factor (cos φ): {power_factor:.2f}")

# Step 4 (Optional): Calculate Phase Angle
phase_angle = cmath.phase(Z)  # In radians
phase_angle_deg = phase_angle * (180 / cmath.pi)  # Convert to degrees
print(f"Phase Angle: {phase_angle_deg:.2f}°")




















