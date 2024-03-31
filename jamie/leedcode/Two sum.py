class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):  # 1.先想兩個數字相加會等於target
              for j in range(i + 1, len(nums)):  # 2.這兩個數字可以用兩種英文代替
                  if nums[i] + nums[j] == target:
                    return [i, j]  # 3.最後在return出這兩個英文代表的數字
        return[]
