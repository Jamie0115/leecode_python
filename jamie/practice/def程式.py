def f1(n):  # arg->參數
    if n > 0:
        m = f2(n)
    else:
        m = 0
    return m

    pass


def f2(m):
    k = 2 * m
    return k
    pass


n = int(input("Number: "))
r = f1(n)
print(r)
