# done
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = dict()
    for i in range(len(nums)):
        num = nums[i]
        if num in dic:
            return [dic.get(num), i]
        else:
            dic[target - num] = i


print(twoSum([2, 7, 11, 15], 9))
