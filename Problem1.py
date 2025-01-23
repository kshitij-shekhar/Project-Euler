 # https://projecteuler.net/problem=1

 # Find sum of all multiples of 3 or 5 below 1000


multiples=[]
for i in range(1,1000):
   if i%5==0 or i%3==0:
       multiples.append(i)
# for i in range(10):
    # print(multiples[i])
print("Sum of all multiples below 1000 : ", sum(multiples))