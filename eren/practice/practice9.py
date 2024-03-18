# 1. a % b 取餘數n
# 2. 判斷餘數n是否為0
# 2.1 是,=0，最大公因數為b
# 2.2 否,<>0, 取 b % n的餘數=>step1

def gcd(a, b):
    if a > b:
        n = a % b
        if n == 0:
            return b
        else:
            return gcd(b, n)
    else:
        return gcd(b, a)


x = int(input("Input x:"))
y = int(input("Input y:"))

print(gcd(x, y))
