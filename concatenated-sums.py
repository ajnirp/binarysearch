# https://binarysearch.com/problems/Concatenated-Sums

# INCOMPLETE - TLE on large input

class Solution:
    def solve(self, nums):
        return sum(int(str(n) + str(m)) for n in nums for m in nums)