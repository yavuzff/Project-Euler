#Problem 26

def reciprocal(n):
    answer = 1/n
    decimal = str(answer)[2:]
    repeat = []
    for i in decimal:
        if i not in repeat:
            repeat.append(i)
        else:
            break
    return len(repeat)

def decimal(n):
     dividend = 1
     answer = ''
     while dividend:
         answer += str(dividend//n)
         dividend = dividend%n *  10
         if len(answer) == 2*n-1:
             return answer
     return answer

max = 1
for i in range (2,1001):
    current = decimal(i)[1:]
    half = current[:i-1]
    if current[i-1:]==half:
        quarter = half[:len(half)//2]
        if quarter != half[len(half)//2:]:
            max = i

print(max)

