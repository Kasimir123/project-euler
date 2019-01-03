# Solution for Project Euler Problem 3

# Import Functions
from functions import *

# Constants:
largest_digit_number = 999
largest_digit_number_two = 999
smallest_digit_number = 100
palindrome = []

# Main 
n = largest_digit_number * largest_digit_number_two
x = smallest_digit_number ** 2
while n >= x:
    while largest_digit_number_two > smallest_digit_number:

        if check_if_palindrome(n) == True:
            palindrome.append(n)
        
        largest_digit_number_two -= 1
        n = largest_digit_number * largest_digit_number_two
    largest_digit_number_two = 999
    largest_digit_number -= 1



palindrome.sort()    
print(palindrome)