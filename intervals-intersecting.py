# https://binarysearch.com/problems/Intervals-Intersecting-at-Point

class Solution:
    def solve(self, intervals, point):
        return sum(a <= point <= b for (a, b) in intervals)
