#Problem 10

def isPrime(num):
    sqrt = int(num**0.5)

    for i in range (2,sqrt+1):
        if num % i == 0:
            return False
    return True

target = 2*10**6
total = 0
current = 2

while current< target:
    if isPrime(current):
        total += current
    current += 1

print(total)
