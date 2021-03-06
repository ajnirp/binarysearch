# https://binarysearch.com/problems/Complete-an-Arithmetic-Sequence

class Solution:
    def solve(self, nums):
        l = len(nums)
        d = (nums[-1] - nums[0]) / (len(nums))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != d:
                return nums[i-1] + d