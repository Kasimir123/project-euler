# Solution for Project Euler Problem 1

# Set up constants:
total_sum = 0
max_num = 1000
current = 0

# Set up loop
while current < max_num:
    if (current % 3) == 0:
        total_sum = total_sum + current
    elif (current % 5) == 0:
        total_sum = total_sum + current
    current += 1
print(total_sum)