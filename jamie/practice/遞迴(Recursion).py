# 直接遞迴
def recur(n):
    if n <= 0:
        return 1
    pre = recur(n-1)
    return pre + n
print(recur(4))
def recur(n):
    if n <= 0:
        return 1
    return recur(n-1) + n
