# https://binarysearch.com/problems/Base-3-to-Integer

class Solution:
    def solve(self, s):
        power_3 = 1
        result = 0
        for c in reversed(s):
            result += int(c) * power_3
            power_3 *= 3
        return result