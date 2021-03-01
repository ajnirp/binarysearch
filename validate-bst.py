# https://binarysearch.com/problems/Binary-Search-Tree-Validation

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, min_, max_):
        if not node:
            return True
        left_recur = self.helper(node.left, min_, node.val)
        right_recur = self.helper(node.right, node.val, max_)
        self_check = min_ < node.val < max_
        return self_check and left_recur and right_recur

    def solve(self, root):
        return self.helper(root, -1e20, 1e20)