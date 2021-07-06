#Problem 21


def factorSum(num): #gives the sum of proper divisors of n, n>1
    upper = int(num**0.5)
    total = 1
    for i in range(2,upper+1):
        if num % i == 0:
            total += i
            total += num//i

    return total

pairs = []
total = 0

visiting = [True]*9999
current = 1

for i in range (1,10000):
    currentSum = factorSum(i)
    visiting[i-1] = False
    if currentSum > 9999 or visiting[currentSum-1] == False:
        continue
    nextSum = factorSum(currentSum)
    if nextSum == i:
        pairs.append((i,currentSum))
        total += i+currentSum
        visiting[currentSum-1]=False
        continue
print(total)
