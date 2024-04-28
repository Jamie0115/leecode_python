# done
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        array = list()
        while x > 0:
            array.append(x % 10)
            x = x // 10

        leftIndex = 0
        rightIndex = len(array) - 1
        while leftIndex < rightIndex:
            if array[leftIndex] != array[rightIndex]:
                return False
            else:
                leftIndex = leftIndex + 1
                rightIndex = rightIndex - 1
        return True


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
