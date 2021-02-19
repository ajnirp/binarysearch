# https://binarysearch.com/problems/Rotation-of-Another-String

class Solution:
    def solve(self, s0, s1):
        return len(s0) == len(s1) and s0 in s1 + s1