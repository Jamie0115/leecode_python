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

        start = 0
        end = len(array) - 1
        while start < end:
            if array[start] != array[end]:
                return False
            else:
                start = start + 1
                end = end - 1
        return True


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
