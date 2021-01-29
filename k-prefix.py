# https://binarysearch.com/problems/K-Prefix

from itertools import accumulate

class Solution:
    def solve(self, nums, k):
        prefix = list(accumulate(nums))

        # find rightmost element of prefix that is <= k
        for i in range(len(prefix)-1, -1, -1):
            if prefix[i] <= k:
                return i

        return -1