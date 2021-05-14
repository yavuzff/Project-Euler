#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primeFactors(num):
    sqrt = int(num**0.5)
    primefactors = {}

    for i in range (2,sqrt+1):
        while num % i == 0:
            num = num/i
            primefactors[i] = primefactors.get(i,0) + 1
    if num != 1:
        primefactors[num] = 1
    return primefactors

target = 20
finalFactors = {}

for i in range (2,target + 1):
    factors = primeFactors(i)
    for k,v in factors.items():
      if finalFactors.get(k,0) < v:
          finalFactors[k] = v

print(finalFactors)

answer = 1
for k,v in finalFactors.items():
    answer *= k**v

print(answer)
