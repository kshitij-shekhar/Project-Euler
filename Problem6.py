# https://projecteuler.net/problem=6

sum_of_squares=0
for i in range(1,101):
    sum_of_squares+=i**2

square_of_sum=0
for j in range(1,101):
    square_of_sum+=j

square_of_sum=square_of_sum**2

print(sum_of_squares-square_of_sum)