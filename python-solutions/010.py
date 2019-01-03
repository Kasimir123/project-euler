# Solution for Project Euler Problem 10

# Import Functions
from functions import *

# Constants:
n = 2000000
count = 2
prime_count = 0
total_sum = 0

# Main 
while count <= n:
    if check_if_prime(count) == True:
        total_sum += count
    count += 1
    print(count)
print(total_sum)