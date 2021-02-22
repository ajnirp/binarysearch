# https://binarysearch.com/problems/Sorted-Elements

class Solution:
    def solve(self, nums):
        nums_sorted = list(sorted(nums))
        return sum(a == b for a, b in zip(nums, nums_sorted))