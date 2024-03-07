"""
print("Hello World!")
string = input("Enter: ")
print("Hello, " + string)
str1 = int(input("Enter: "))
str2 = int(input("Enter: "))
print(str1 + str2)
str3 = int(input("Enter: "))
if str3 % 2 == 1:
    print("odd")
else:
    print("even")

import random
sum = [0, 0, 0]  # 餘0、餘1和餘2分別有幾個
for i in range(random.randint(1,10)):
    sum[int(input("input:")) % 3] += 1

print(','.join([str(i) for i in sum]))  # join只能用字串串起來
"""

