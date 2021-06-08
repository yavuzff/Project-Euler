def seqNext(num):
    if num % 2 == 0:
        return num//2
    else:
        return 3*num+1

memoization = {1:1}
maxStart = 0
maxChain = 0

for i in range (1,1*10**6+1):
    start = i
    chain = 0
    while i not in memoization:
        i = seqNext(i)
        chain += 1
    chain += memoization[i]
    memoization[start]=chain
    if chain > maxChain:
        maxChain = chain
        maxStart = start
print(maxStart)


