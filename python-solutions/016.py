# Solution for Project Euler Problem 16

# Import Functions
from functions import *

# Constants:
x = 2
exponent = 1000
total_sum = 0
digits = str(x ** exponent)

# Main 
for i in range(len(digits)):
    total_sum += int(digits[i])
print(total_sum)