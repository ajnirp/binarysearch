# https://binarysearch.com/problems/Minimum-Cost-Sort

class Solution:
    def ascending_cost(self, nums):
        s_nums = list(sorted(nums))
        return sum(abs(a-b) for a, b in zip(nums, s_nums))

    def descending_cost(self, nums):
        s_nums = list(sorted(nums, reverse=True))
        return sum(abs(a-b) for a, b in zip(nums, s_nums))

    def solve(self, nums):
        return min(self.ascending_cost(nums), self.descending_cost(nums))