#Problem 20

from math import factorial
num = 100
total = 0
for i in str (factorial(num)):
    total += int(i)
print(total)
