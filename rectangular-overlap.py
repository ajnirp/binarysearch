# https://binarysearch.com/problems/Rectangular-Overlap

# point lies in rectangle
def in_(self, p, r):
    return r[0] < p[0] < r[2] and r[1] < p[1] < r[3]

class Solution:
    # at least one vertex of rectangle s lies in rectangle r
    def at_least_one_point_lies_in_other(self, s, r):
        return in_(self, (s[0], s[1]), r) or in_(self, (s[2], s[3]), r) or in_(self, (s[0], s[3]), r) or in_(self, (s[2], s[1]), r)

    # two rectangles overlap
    def solve(self, s, r):
        return self.at_least_one_point_lies_in_other(s, r) or self.at_least_one_point_lies_in_other(r, s)
