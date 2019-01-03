# Find all factors
def find_factors(number):
    array = []
    i = 1
    while i <= int(number**0.5)+1:
        if number % i == 0:
            x = number // i
            if x != i:
                array.extend((i,x))
            else:
                array.append(i)
        i += 1
    return array

# Create Fibonacci array
def fibonacci_generation(max_digit):
    current_fibonacci = 1
    fibonacci = [1,2]
    while fibonacci[current_fibonacci] < max_digit:
        fibonacci.append(fibonacci[current_fibonacci] + fibonacci[current_fibonacci - 1])
        current_fibonacci += 1
    return fibonacci

# Checks if the number is prime
#   currently only checks positives
def check_if_prime(n):
    if n > 10:
        x = n % 10
        if x in [0, 2, 4, 5, 6, 8] or n % 3 == 0:
            return False
        else:
            factors = find_factors(n)
            if len(factors) != 2:
                return False
    elif n in [4, 6, 8, 9, 10]:
        return False
    return True

# Check if number is a palindromic number
def check_if_palindrome(n):
    x = str(n)[::-1]
    if n == int(x):
        return True
    else:
        return False

# Checks if a number can be divided by another number without a remainder
def check_remainder(n, divider):
    if n % divider == 0:
        return True
    else: 
        return False

# Sum of Squares for n'th digit
def sum_of_squares(n):
    total_sum = 0
    while n > 0:
        total_sum += n ** 2
        n -= 1
    return total_sum

# Square of sum till n'th digit
def square_of_sums(n):
    total_sum = 0
    while n > 0:
        total_sum += n
        n -= 1
    return total_sum ** 2