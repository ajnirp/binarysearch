# https://binarysearch.com/problems/List-Equality-with-Increments

# the greedy approach works (fix the max, increment the rest).
# now, an observation - you'll get the same number of steps if you flip everything
# i.e. you only *decrement* the max each time.
# when do you stop decrementing? when everyone's equal to the minimum.

class Solution:
    def solve(self, nums):
        m = min(nums)
        res = 0
        for num in nums:
            res += num - m
        return res