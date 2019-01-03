# Solution for Project Euler Problem 5

# Import Functions
from functions import *

# Constants:
i = 1

# Main 
while True:
    n = i * 20
    if check_remainder(n, 2) == True:
        if check_remainder(n, 3) == True:
            if check_remainder(n, 4) == True:
                if check_remainder(n, 5) == True:
                    if check_remainder(n, 6) == True:
                        if check_remainder(n, 7) == True:
                            if check_remainder(n, 8) == True:
                                if check_remainder(n, 9) == True:
                                    if check_remainder(n, 10) == True:
                                        if check_remainder(n, 11) == True:
                                            if check_remainder(n, 12) == True:
                                                if check_remainder(n, 13) == True:
                                                    if check_remainder(n, 14) == True:
                                                        if check_remainder(n, 15) == True:
                                                            if check_remainder(n, 16) == True:
                                                                if check_remainder(n, 17) == True:
                                                                    if check_remainder(n, 19) == True:
                                                                        print(n)
                                                                        break
    i += 1