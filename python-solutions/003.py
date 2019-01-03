# Solution for Project Euler Problem 3

# Import Functions
from functions import *

# Constants:
number = 600851475143
largest_prime = 0

# Main 
factors = find_factors(number)
for each in factors:
    if check_if_prime(each) == True:
        if each > largest_prime:
            largest_prime = each
print(largest_prime)