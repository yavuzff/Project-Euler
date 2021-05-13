def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])

    else: return False

def doesFactor(num):
    for i in range (100,1000):
        factor = num/i
        if factor.is_integer() and len(str(int(factor))) == 3:
            print(factor,i)
            return True
num = 1000000
found = False

while not found:
    if isPalindrome(str(num)) and doesFactor(num):
        print(num)
        found = True
    else:
        num -= 1

