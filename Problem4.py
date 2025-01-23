#https://projecteuler.net/problem=4

#find the largest palindrome formed by the multiplication of two 3-digit numbers

# print(str(9009)[::-1]==str(9090))
palindromes=[]
for i in range(100,1000):
    for j in range(100,1000):
        if str(i*j)==str(i*j)[::-1]:
            palindromes.append(i*j)

print(max(palindromes))
