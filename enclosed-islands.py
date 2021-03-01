# https://binarysearch.com/problems/Enclosed-Islands

# do a dfs from every 1 that's on an edge. then count all 1's that haven't
# been seen by any of those dfs's.

class Solution:
    def bounds(self, matrix, r, c):
        return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

    def dfs(self, matrix, r, c):
        if not self.bounds(matrix, r, c):
            return
        if matrix[r][c] == 0:
            return
        if (r, c) in self.seen:
            return
        self.seen.add((r, c))
        nbrs = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for nbr in nbrs:
            self.dfs(matrix, nbr[0], nbr[1])

    def solve(self, matrix):
        self.seen = set()
        for col in range(len(matrix[0])):
            self.dfs(matrix, 0, col)
            self.dfs(matrix, len(matrix)-1, col)
        for row in range(len(matrix)):
            self.dfs(matrix, row, 0)
            self.dfs(matrix, row, len(matrix[0])-1)
        result = 0
        for row in range(1, len(matrix)-1):
            for col in range(1, len(matrix[0])-1):
                if matrix[row][col] == 1 and (row, col) not in self.seen:
                    result += 1
        return result

matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

print(Solution().solve(matrix)) # expected: 4