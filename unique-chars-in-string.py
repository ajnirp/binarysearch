# https://binarysearch.com/problems/A-Unique-String

class Solution:
    def solve(self, s):
        return len(s) == len(set(s))