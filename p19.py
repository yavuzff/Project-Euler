#Problem 19

def nextYear(currentDay,leap):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap:
        months[1] = 29

    count = 0

    for i in range(0,len(months)):
        currentDay = (currentDay+months[i]) % 7
        if currentDay == 6: #start of next month
            count += 1

    return (count,currentDay)

total = 0
firstday = 1
for year in range (1901,2001):
    leap = False
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        leap = True

    result = nextYear(firstday,leap)
    total += result[0]
    firstday = result[1]

print(total)
