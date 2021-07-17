def factorSum(num): #gives the sum of proper divisors of n, n>1
    upper = int(num**0.5)
    total = 1
    for i in range(2,upper+1):
        if num % i == 0:
            if num//i == i:
                total += i
            else:
                total += i
                total += num//i

    return total

def isAbundant(num):
    if factorSum(num) > num:
        return True
    else:
        return False

upper = 28123
abundantNums = []
for i in range (1,upper+1):
    if isAbundant(i):
        abundantNums.append(i)

sumOf2 = {}
#for i in range (0,len(abundantNums)):
    #for j in range(i+1,len(abundantNums)):
for i in range(0,len(abundantNums)):
    for j in range(i,len(abundantNums)):
        val = abundantNums[i]+abundantNums[j]
        if val <= upper:
            sumOf2[val]=1
#print(abundantNums)
#print(sumOf2)

total = 0
for i in range (1,upper+1):
    if i not in sumOf2:
        total+=i
print(total)
4179935
