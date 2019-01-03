# Solution for Project Euler Problem 2

# Constants:
max_digit = 4000000
fibonacci = [1,2]
current_fibonacci = 1
total_sum = 0

# Create Fibonacci array
def fibonacci_generation():
    global fibonacci, current_fibonacci
    while fibonacci[current_fibonacci] < max_digit:
        fibonacci.append(fibonacci[current_fibonacci] + fibonacci[current_fibonacci - 1])
        current_fibonacci += 1

# Find sum of even valued terms
fibonacci_generation()
for term in fibonacci:
    if term < max_digit and (term % 2) == 0:
        total_sum += term
print(total_sum)