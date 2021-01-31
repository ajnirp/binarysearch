# https://binarysearch.com/problems/Vertical-Lines-in-Binary-Tree

# idea: just store the net "shift" as a parameter to the recursive call,
# and at each node, if it exists, update the max tree shift and min tree shift

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, shift):
        if node is None:
            return
        self.min = min(self.min, shift)
        self.max = max(self.max, shift)
        self.helper(node.left, shift-1)
        self.helper(node.right, shift+1)

    def solve(self, root):
        if root is None:
            return 0
        self.min = 0
        self.max = 0
        self.helper(root, 0)
        return self.max - self.min + 1