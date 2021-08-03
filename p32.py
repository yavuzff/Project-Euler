#Problem 32

def isPandigital(n):
    digits = len(str(n))
    count = [0]*digits

    for i in str(n):
        if not 1<=int(i)<=digits:
            return False
        if count[int(i)-1] == 1:
            return False
        else:
            count[int(i)-1] += 1
    return True



nums = {}
for i in range (0,10000):
        #for j in range (0,10000):
        for j in range(0,10**(5-len(str(i)))):
            combined = str(i)+str(j)+str(i*j)
            if len(combined) == 9 and isPandigital(combined):
                nums[i*j] = True

print (sum(nums.keys()))
