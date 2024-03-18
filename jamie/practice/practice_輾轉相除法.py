def num(c1, c2):  # num() -> 是一個method，在外面呼叫數字進去算自己的方程式
    if c1 > c2:
        n = c1 % c2  # 取c1和c2的餘數
        if n == 0:  # 如果餘數等於0
            return c2  # 最大公因數為c2
        else:
            return num(c2, n)  # 如果不等於0
    else:
        return num(c2, c1)


a1 = int(input("input: "))
b1 = int(input("input: "))
print(num(a1, b1))
