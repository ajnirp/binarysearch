# https://binarysearch.com/problems/N-Rooks

class Solution:
    def solve(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result