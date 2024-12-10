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



import matplotlib.pyplot as plt

# List of complex numbers
complex_numbers = [1+1j, 2+2j, 3-1j, -1-1j]

# Plot real vs imaginary parts
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(color='lightgray', linestyle='--')

for z in complex_numbers:
    plt.plot(z.real, z.imag, 'ro')
    plt.text(z.real, z.imag, f" {z}")

plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.title("Complex Numbers")
plt.show()




def mandelbrot(c, max_iterations):
    z = 0 + 0j
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:  # Escape condition
            return i
    return max_iterations

c = -0.7 + 0.27015j
iterations = mandelbrot(c, 1000)
print(f"Mandelbrot iterations: {iterations}")


import cmath

# Solving ax^2 + bx + c = 0
a, b, c = 1, 2, 5
discriminant = cmath.sqrt(b**2 - 4*a*c)

root1 = (-b + discriminant) / (2 * a)
root2 = (-b - discriminant) / (2 * a)

print(f"Root 1: {root1}")  # Output: (-1+2j)
print(f"Root 2: {root2}")  # Output: (-1-2j)



import cmath

# Magnitude and phase
z = 1 + 1j
magnitude = abs(z)  # Magnitude of the complex number
phase = cmath.phase(z)  # Phase angle in radians

print(f"Magnitude: {magnitude}")  # Output: 1.4142135623730951
print(f"Phase: {phase}")          # Output: 0.7853981633974483

# Converting from polar to rectangular form
r = 2
theta = cmath.pi / 4
z_polar = cmath.rect(r, theta)  # Returns 2 * (cos(theta) + j*sin(theta))
print(f"Polar to Rectangular: {z_polar}")  # Output: (1.4142135623730951+1.4142135623730951j)



