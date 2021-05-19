# Problem 7 
#see: Sieve of Erathosthenes

def isPrime(num):
    sqrt = int(num**0.5)

    for i in range (2,sqrt+1):
        if num % i == 0:
            return False
    return True

target = 10001
primes = 0
current = 2
while primes< target:
    if isPrime(current):
        primes += 1
    current += 1
print(current-1)


