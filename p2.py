#project euler problem 2

total = 0
num1 = 1
num2 = 2

while num1 <= 4*10**6:
    if num1 % 2 == 0:
        total += num1
    temp = num1
    num1 = num2
    num2 += temp

print(total)


