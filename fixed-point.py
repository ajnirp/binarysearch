# https://binarysearch.com/problems/Fixed-Point

# the array elements are unique and also integers so going left to right
# you increase by at least 1 on each step
# which means that nums[i] - i is non-decreasing. so binary search applies
# to it

class Solution:
    def helper(self, nums, lo, hi):
        if lo > hi:
            return -1

        if lo == hi:
            return lo if nums[lo] == lo else -1

        mid = lo + ((hi - lo) // 2)
        if nums[mid] == mid: # go left just to be safe
            return self.helper(nums, lo, mid)
        elif nums[mid] > mid: # go left
            return self.helper(nums, lo, mid-1)
        else: # go right
            return self.helper(nums, mid+1, hi)

    def solve(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

