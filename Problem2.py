# https://projecteuler.net/problem=2

# Find sum of even valued terms in a fibonacci sequence upto 4,000,000

fibo=[1,2]


while fibo[-1]<=4000000:
    fibo.append(fibo[-1]+fibo[-2])

# last element in the sequence exceeds 4 million
fibo.pop()

#find sum of all even terms in the list
sum=0
for i in fibo:
    if i%2==0:
        sum+=i
print(sum)

