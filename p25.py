
num1 = 0
num2 = 1
fn = 1

while len(str(num2))< 1000:
    temp = num1
    num1 = num2
    num2 += temp
    fn += 1
print(fn)
