#Problem 30

def digitsPowers(num):
    total = 0
    for i in str(num):
        total += fifthpowers[int(i)]
    return total

fifthpowers = {}
for i in range(0,10):
    fifthpowers[i] = i**5

total = 0
for i in range (10,1000000):
    if i == digitsPowers(i):
        total += i
print(total)
443839
