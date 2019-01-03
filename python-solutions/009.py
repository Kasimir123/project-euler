# Solution for Project Euler Problem 9

# Import Functions
from functions import *

# Constants:
number = 1000
a = 1
c = 997
b = number - c - a
new_a = 0
new_b = 0
new_c = 0
run = True

# Main 
while run:
    while c > b:
        if pythagorean_triplet(a,b,c):
            new_a = a
            new_b = b
            new_c = c
            print(new_a * new_b * new_c)
            run = False
            break
        else:
            c -= 1
            b = number - c -a
    a += 1
    c = 998 - a
    b = number - c -a