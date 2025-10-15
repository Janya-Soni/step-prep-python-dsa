class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in dt:
                return [dt[val], i]
            dt[num] = i