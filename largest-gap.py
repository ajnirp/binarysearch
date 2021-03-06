# https://binarysearch.com/problems/Largest-Gap

class Solution:
    def solve(self, nums):
        nums.sort()
        return max(nums[i] - nums[i-1] for i in range(1, len(nums)))