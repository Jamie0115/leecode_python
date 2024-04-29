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