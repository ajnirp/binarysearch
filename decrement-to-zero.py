# https://binarysearch.com/problems/Number-of-Operations-to-Decrement-Target-to-Zero

# INCOMPLETE TLE

class Solution:
    def helper(self, nums, lo, hi, target):
        if target == 0:
            return True, 0
        if lo > hi:
            if target == 0:
                return True, 0
            else:
                return False, -1
        if (target, lo, hi) not in self.dp:
            take_lo = self.helper(nums, lo+1, hi, target - nums[lo])
            take_hi = self.helper(nums, lo, hi-1, target - nums[hi])
            self.dp[(target, lo, hi)] = take_lo[0] or take_hi[0], 1 + min(take_lo[1], take_hi[1])
        return self.dp[(target, lo, hi)]

    def solve(self, nums, target):
        if nums == []:
            return 0 if target == 0 else -1
        self.dp = {}
        possible, ans = self.helper(nums, 0, len(nums)-1, target)
        if possible:
            return ans
        return -1
