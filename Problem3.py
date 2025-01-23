# https://projecteuler.net/problem=3

# Find largest prime factor of 600851475143

def is_prime(num):
    """Returns 1 if num is prime, 0 if it isn't"""
    for i in range(2,num//2):
        if num%i==0:
            return 0
    return 1




result=600851475143
prime_factors=[]
for i in range(2,600851475143):
    if result==1:
        break
    if is_prime(i)==1:
        if result%i==0:
            result=result/i
            prime_factors.append(i)

print(max(prime_factors))
