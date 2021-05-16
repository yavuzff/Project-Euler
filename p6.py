#Project Euler Problem 6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nums = 100
squaresum = 0
sum = 0

for i in range (1,101):
    squaresum += i**2
    sum += i

sumsquared = sum**2

print(abs(squaresum-sumsquared))

