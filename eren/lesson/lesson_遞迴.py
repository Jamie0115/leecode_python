# n階乘
# 5! => 5 * 4! => 5 * 4 * 3! => 5 * 4 * 3 * 2! => 5 * 4 * 3 * 2 * 1
# => n * (n-1)! => (n-1) * (n-2)!
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n == 1:
        return 1


# 費氏數列
# 0,1,1,2,3,5,8,13,21,34,55,...
def fib(n):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0


num = int(input('Input a number:'))

# print(factorial(num))
print(fib(num))


# 60 , 48
n = 60 % 48
