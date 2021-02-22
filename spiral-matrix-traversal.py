# https://binarysearch.com/problems/Spiral-Matrix

class Solution:
    def helper(self, matrix, x0, y0, x1, y1):
        if x0 > x1 or y0 > y1:
            return
        # y = y0, x runs from x0 to x1
        for x in range(x0, x1+1):
            self.result.append(matrix[y0][x])
        # x = x1, y runs from y0+1 to y1
        for y in range(y0+1, y1+1):
            self.result.append(matrix[y][x1])
        if y1 > y0:
            # y = y1, x runs from x1-1 to x0
            for x in range(x1-1, x0-1, -1):
                self.result.append(matrix[y1][x])
        if x1 > x0:
            # x = x0, y runs from y1 to y0+1
            for y in range(y1-1, y0, -1):
                self.result.append(matrix[y][x0])
        self.helper(matrix, x0+1, y0+1, x1-1, y1-1)

    def solve(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        self.result = []
        self.helper(matrix, 0, 0, len(matrix[0])-1, len(matrix)-1)
        return self.result

matrix = [
    [6, 9, 8],
    [1, 8, 0],
    [5, 1, 2],
    [8, 0, 3],
    [1, 6, 4],
    [8, 8, 10]
]

print(Solution().solve(matrix))