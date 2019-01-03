# Solution for Project Euler Problem 12

# Import Functions
from functions import *

# Constants:
divisors = 500
run = True
i = 1

# Main 
while run:
    triangle_num = triangle_number(i)
    if len(find_factors(triangle_num)) >= 500:
        print(triangle_num)
        break
    else:
        i += 1
