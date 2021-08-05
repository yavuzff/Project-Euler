#Problem 33

from fractions import Fraction

def simplify(a,b):
    for i in a:
        if i in b:
            return [a[(a.index(i)+1)%2],b[(b.index(i)+1)%2]]
    
    return []


fraction = ['  ','  ']
curious = []
for num1 in range (11,100):
    for num2 in range (num1+1, 100):
        if str(num1)[1] != '0' and str(num2)[1] != '0':
            simplified = simplify(str(num1),str(num2))
            if simplified:
                if Fraction(num1,num2) == Fraction(int(simplified[0]),int(simplified[1])):
                    print(num1,num2)
                    curious.append(Fraction(num1,num2))


product = 1
for i in curious:
    product *= i

print(product)

                
                
                
