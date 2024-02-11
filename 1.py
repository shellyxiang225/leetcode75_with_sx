class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i, num in  enumerate(nums):
            completment = target - num
            if completment in index:
                return [index[completment],i]
            index[num] = i
        return []

