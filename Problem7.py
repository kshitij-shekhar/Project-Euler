# https://projecteuler.net/problem=7

# Print 10,001st Prime number
import math
def is_prime(num):
    """Returns 1 if num is prime, 0 if it isn't"""
    for i in range(2,int(math.sqrt(num)) + 1):
        if num%i==0:
            return 0
    return 1

num=2
count=0

while count<=10001:
    if is_prime(num)==1:
        count+=1
        if count==10001:
            break
    
    num+=1

print(num)



