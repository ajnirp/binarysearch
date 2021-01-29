# https://binarysearch.com/problems/Smallest-Pair-Sum-with-Distance-Constraint

class Solution:
    def solve(self, nums):
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(min(prefix[-1], num))

        return min(nums[idx] + prefix[idx-2] for idx in range(2, len(nums)))