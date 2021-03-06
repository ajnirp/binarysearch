# https://binarysearch.com/problems/Ugly-Number

# idea: remove all the 2s, 3s, and 5s from the number. You should be left with
# 1. Otherwise it's not an "ugly" number.

class Solution:
    def solve(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1