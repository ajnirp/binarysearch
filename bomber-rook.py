# https://binarysearch.com/problems/Bomber-Man

# solution based on a simple observation: if you swap two rows in a chessboard
# the number of "safe" squares remains constant. same for columns. so we just
# "move" all the rook-occupied rows and columns to any one corner of the chessboard,
# say the top left, and then the square at the bottom right with no rooks on it
# is completely safe

class Solution:
    def solve(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        unsafe_rows = set()
        unsafe_cols = set()
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 1:
                    unsafe_rows.add(r)
                    unsafe_cols.add(c)
        return (len(matrix) - len(unsafe_rows)) * (len(matrix[0]) - len(unsafe_cols))