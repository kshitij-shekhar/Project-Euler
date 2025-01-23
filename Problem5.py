#https://projecteuler.net/problem=5

# divisors=[i for i in range(1,21)]

# start=20

# while start>=20:
#     duplicate=start #flag to check if start has been updated => start is not evenly divisible by atleast one divisor
#     # print(duplicate)
#     for d in divisors:
#         if start%d!=0:
#             print(start,"isn't evenly divisible by",d)
#             # if start isn't evenly divisible by even a single divisor, increment start and go to next iteration in while loop
#             start+=1
#             break
#     if duplicate==start:
#         #start IS evenly divisible by all divisors
#         print(start,"is the smallest positive number evenly divisble by all divisors in [1,20]")
#         break


import math
from functools import reduce

def lcm(a, b):
    """Calculate the Least Common Multiple of two numbers."""
    return abs(a * b) // math.gcd(a, b)

def lcm_of_range(n):
    """Calculate the LCM of all numbers from 1 to n."""
    return reduce(lcm, range(1, n + 1))

# Find the smallest positive number evenly divisible by each number from 1 to 20
result = lcm_of_range(20)
print(f"The smallest positive number evenly divisible by each number from 1 to 20 is: {result}")

    

