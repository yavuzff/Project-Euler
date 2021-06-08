#Project Euler problem 3

num = 600851475143
sqrt = int(num**0.5)
primefactors = {}

for i in range (2,sqrt):
    while num % i == 0:
        num = num/i
        primefactors[i] = 1
if num != 1:
    print(num)
else:
    print(max(primefactors.keys()))

