#  1. 判斷是否為質數
def num(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True  # return 在外面要先跑過一輪再判斷是否為質數


#  2. 輸入n值，得出2~n的質數
count = int(input("Input number: "))
prime = []
for j in range(2, count + 1):
    is_prime = num(j)
    if is_prime:
        prime.append(j)
print(prime)
