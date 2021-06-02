#Problem 12

def returnFactors(num):
    sqrt = int(num**0.5)
    divisors = 0
    for i in range (1,sqrt+1):
        if num % i == 0:
            if num/i == i:
                divisors += 1
            else:
                divisors += 2
    return divisors


def p12():
    current = 1
    add = 2

    while True:
        if returnFactors(current) > 500:
            return current
        else:
            current += add
            add += 1

print(p12())
