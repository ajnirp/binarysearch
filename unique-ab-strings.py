# https://binarysearch.com/problems/Unique-Ab-Strings

# count number of 'a's and raise 2 to that power

class Solution:
    def solve(self, s):
        return 1 << sum(c == 'a' for c in s)