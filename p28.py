#Project Euler problem 28

# 9,25,49
#  16 24
#   8 -> 4n^2 -> 4, 16, 36
# 4n^2 + 4n + 1

# 5 17 37
#  12 20
#    8    4n^2 -> 4,16,36
#4n^2+1

# 3 13 31
#  10 18
#    8    4n^2 -> 4,16,36
#4n^2 -2n + 1

# 7 21 43
#  14 22
#    8    4n^2 -> 4,16,36
#4n^2 + 2n + 1

#1001 by 1001
#     500
# 500__|__500 500 right 500 up so 500 to every diagonal
#      |
#      500
n=1001
total = 1
for i in range(1,(n-1)//2+1):
    total += 4*i**2 + 4*i +1
    total += 4*i**2 +1
    total += 4*i**2 - 2*i +1
    total += 4*i**2 + 2*i +1
print(total)


