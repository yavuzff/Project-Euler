def isPrime(num):
    sqrt = int(num**0.5)

    for i in range (2,sqrt+1):
        if num % i == 0:
            return False
    return True

def primeLength(a,b):
    n = 0
    while (n**2 + a*n + b) in primes:
        n+=1
    return n

primes = {}
for i in range (1,1000):
    if isPrime(i) and i != 1:
        primes[i] = 1

maximum = 0
maxab = [0,0]
print(primes.keys())
for a in range(-999,1000):
    for b in primes.keys():
        length = primeLength(a,b)

        if length>maximum:
            maximum = length
            maxab[0] = a
            maxab[1] = b
print(maximum,maxab)
print(maxab[0]*maxab[1])



