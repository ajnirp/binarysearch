# https://binarysearch.com/problems/Line-Segment

class Solution:
    def slope(self, c1, c2):
        a, b = c1
        c, d = c2
        return 'inf' if a == c else (d - b) / (a - c)

    def solve(self, coordinates):
        if len(coordinates) < 3:
            return True

        slope = self.slope(coordinates[0], coordinates[1])
        return all(slope == self.slope(c, coordinates[0]) for c in coordinates[2:])