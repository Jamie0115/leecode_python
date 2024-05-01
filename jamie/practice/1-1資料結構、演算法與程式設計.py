"""
A = ["好吃的", "好看的", "好玩的"]
B = ["蘋果", "手機"]
for adj in A:
    for noun in B:
        print(adj, noun)
"""
# 99乘法表
"""
def timesTable():
    for r in range(1, 10):
        for i in range(1, 10):
            print(r, "X", i, "=", r*i,end= ", ")
        print()
timesTable()
"""
"""
# 星星金字塔
def starTree(n):
    for i in range(1, n+1):  # 範圍1~n
        for s in range(n-1):  #共n-1次
            print(' ', end = '')
        for c in range(2*i - 1):
            print('*', end = '')
        print()

n = int(input("Number: "))
starTree(n)
"""
"""
sum = 0
for I in range(-5, 101, 7):
    sum = sum + 1
    print(sum)
"""
"""
value = 100
sum = 0
while sum < 300:
    value -= 20
    if value < 0:
        break
    sum += value
print(sum)
"""
"""
def F(x, y):
    k = 0
    for i in range(x, 0, -1):
        print(i)
        for j in range(y, 0, -1):
            print(j)
            k = k + 1
    return k
print(F(3, 1))
"""
"""
# 利用迴圈計算級數: 1 + x/2 + x^2/4 + x^3/8 + x^4/16 + x^5/32, x = 1.4
x = 1
sum = 0
num = 1
for i in range(0, 2):
    sum += num
    num = num * x/2
print(sum)
"""
# 公式:1 - x^2 + x^4/2! - x^6/3! + x^8/4! - x^10/5! + x^12/6!
x = 1
sum = 0
num = 1
factor = 1
for i in range(0, 3):
    print(i)
    factor *= (i + 1)
    sum += num
    num = num * -x**2/factor
print(sum)