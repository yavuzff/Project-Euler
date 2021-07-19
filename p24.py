#Problem 24

from math import factorial

def form(digits,nth):

    if len(digits) == 2:
        return str(digits[nth-1])+str(digits[(nth-1+1)%2])
    ways = factorial(len(digits))
    step = ways/len(digits)
    count = 0
    while not ((step*count) <= nth <= (step*(count+1))):
        count += 1
    start = str(digits[count])
    digits.pop(count)
    return start+form(digits,nth-int(count*step))

print(form([0,1,2,3,4,5,6,7,8,9],10**6))

