def letterVal(letter):
    return ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter)

def wordVal(word):
    total = 0
    for i in word:
        total += letterVal(i)
    return total

myfile = open('p022_names.txt')
data = myfile.read()
myfile.close()

data = list(eval(data))
data.sort()

total = 0
for i in range(0,len(data)):
    total += wordVal(data[i]*(i+1))

print(total)
