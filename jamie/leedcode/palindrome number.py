#  1. 判斷是否為回文數字
#  利用Python的內建 反轉陣列[::-1]
"""
def isPalindrome(x):
    result = str(x)[::-1]
    if str(x) != result:
        return False
    else:
        return True

x = int(input("Number: "))
print(isPalindrome(x))

"""
"""
numbers = int(input("Number: "))
newList = str(numbers)[::-1]  # [::-1]是要list的形式
print(newList)
"""
#  回文數簡單就是左到右，右到左皆相同就是回文數了
x = int(input("Number: "))
if x < 0:
    print(False)
else:
    array = list()
    while x > 0:
        array.append(x % 10)
        x = x // 10
        print(array)
    leftIndex = 0
    rightIndex = len(array) - 1
    print(array[leftIndex], array[rightIndex])
    print(leftIndex, rightIndex)
    while leftIndex < rightIndex:
        if array[leftIndex] != array[rightIndex]:
            print(False)
        else:
            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1
    print(True)
