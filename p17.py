ones = 'one two three four five six seven eight nine '.split()
teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
hundred = 'hundred'

total = 0
#1 to 19:
for i in ones:
    total += len(i)

for i in teens:
    total += len(i)

#20-99:
for i in range (20,100):
    firstDig = int(str(i)[0])
    secondDig = int(str(i)[1])
    total += len(tens[firstDig-2])

    if secondDig != 0:
        total += len(ones[secondDig-1])

#100-999
for i in range (100,1000):
    print(i)
    string = str(i)
    first = int(string[0])
    second = int(string[1])
    third = int(string[2])

    total += len(ones[first-1])
    total += len(hundred)
    print(ones[first-1],hundred)
    if second != 0 or third != 0:
        total += len('and')
        print('and')
    if second == 1:
        total += len(teens[third])
        print(teens[third])
    else:
        if second != 0:
            total += len(tens[second-2])
            print(tens[second-2])
        if third != 0:
            print(ones[third-1])
            total += len(ones[third-1])
    #input()

total += len('onethousand')
print(total)
