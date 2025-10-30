# Author: Divyang Parikh
# Date: 10/30/25
# Problem 4 – Approximation of Pi and comparison with math.pi

import math  # Import math module

# Approximate pi using the Leibniz formula:
# π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
approx_pi = 0
for i in range(100000):
    approx_pi += ((-1) ** i) / (2 * i + 1)

approx_pi *= 4  # Multiply the result by 4 to get π

# Print both values to compare
print("Approximated Pi (using series):", approx_pi)
print("Pi from math module:", math.pi)