# https://binarysearch.com/problems/Longest-Tree-Sum-Path-From-Root-to-Leaf

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # sum_ = sum of path up to but not including this node
    def helper(self, node, sum_, depth):
        if node is None:
            return
        # if leaf, check if deepest leaf yet and if so, update self.result
        if node.left is None and node.right is None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = sum_ + node.val
            elif depth == self.max_depth:
                self.result = max(self.result, sum_ + node.val)
                return
        self.helper(node.left, sum_ + node.val, depth+1)
        self.helper(node.right, sum_ + node.val, depth+1)

    def solve(self, root):
        if root is None:
            return 0
        self.result = 0
        self.max_depth = 0
        self.helper(root, 0, 0)
        return self.result
