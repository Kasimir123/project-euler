# Solution for Project Euler Problem 2

# Import Functions
from functions import *

# Constants:
max_digit = 4000000
fibonacci = []
total_sum = 0

# Find sum of even valued terms
fibonacci = fibonacci_generation(max_digit)
for term in fibonacci:
    if term < max_digit and (term % 2) == 0:
        total_sum += term
print(total_sum)