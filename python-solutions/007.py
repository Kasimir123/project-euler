# Solution for Project Euler Problem 7

# Import Functions
from functions import *

# Constants:
n = 10001
prime = []
count = 2
prime_count = 0

# Main 
while prime_count != n:
    if check_if_prime(count) == True:
        prime.append(count)
        prime_count += 1
    count += 1
print(prime[n-1])