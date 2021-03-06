# https://binarysearch.com/problems/Arithmetic-Sequence-Permutation

# iff an AP exists, without loss of generality, the sequence can be ascending-sorted

class Solution:
    def solve(self, nums):
        if len(nums) < 3:
            return True
        nums.sort()
        diff = nums[0] - nums[1]
        return all(nums[i] - nums[i+1] == diff for i in range(1, len(nums)-1))