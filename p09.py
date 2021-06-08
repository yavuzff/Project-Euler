#Problem 9

def findSolution():
    for a in range (1,999):
        upper = min(a,1000-a)
        for b in range (1,upper):
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print(a,b,c)
                return a*b*c

print(findSolution())
