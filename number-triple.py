# https://binarysearch.com/problems/A-Number-and-Its-Triple

from collections import Counter

class Solution:
    def solve(self, nums):
        count = Counter(nums)
        for n in count:
            if n == 0:
                if count[0] > 1:
                    return True
            elif 3*n in count:
                return True
        return False