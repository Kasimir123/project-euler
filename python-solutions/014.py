# Solution for Project Euler Problem 14

# Import Functions
from functions import *

# Constants:
i = 1000000
longest_chain_length = 1
longest_chain_number = 1

# Main 
while i > 0:
    if collatz(i) > longest_chain_length:
        longest_chain_length = collatz(i)
        longest_chain_number = i
    i -= 1

print(longest_chain_number)