# https://binarysearch.com/problems/Island-Shape-Perimeter

class Solution:
    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors(self, r, c):
        dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(r+dr, c+dc) for dr, dc in dx if self.in_bounds(r+dr, c+dc)]


    def solve(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        result = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.matrix[r][c] == 0:
                    continue
                nbrs = self.neighbors(r, c)
                result += 4 - sum(self.matrix[r_][c_] == 1 for r_, c_ in nbrs)
        return result

matrix = [
    [0, 1, 1],
    [0, 1, 0]
]
print(Solution().solve(matrix))