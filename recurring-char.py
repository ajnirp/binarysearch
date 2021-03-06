# https://binarysearch.com/problems/Recurring-Character

class Solution:
    def solve(self, s):
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                return i
            seen.add(c)
        return -1