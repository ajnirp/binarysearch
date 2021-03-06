# https://binarysearch.com/problems/Even-Frequency

# INCOMPLETE: can i do this in-place?

from collections import Counter

class Solution:
    def solve(self, nums):
        c = Counter(nums)
        for k in c:
            if c[k] % 2 != 0:
                return False
        return True