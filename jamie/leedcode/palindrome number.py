def isPalindrome(x):
    x = int()
    boo = False
    result = x
    temp = 0
    if x < 0:  # 先判斷是否為正數
        return boo
    while result != 0:  # 確認是正數後代入演算法
        temp = temp * 10 + result % 10
        result = result // 10
    if temp == x:
        boo = True
    return boo


print(isPalindrome(12545456))
