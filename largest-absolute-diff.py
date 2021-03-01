# https://binarysearch.com/problems/Largest-Difference-Between-Node-and-a-Descendant

# INCOMPLETE: i'm computing global max - min, which is wrong

class Solution:
    def helper(self, node):
        if not node:
            return
        self.min_ = min(self.min_, node.val)
        self.max_ = max(self.max_, node.val)
        self.helper(node.left)
        self.helper(node.right)

    def solve(self, root):
        if not root:
            return 0
        self.min_ = root.val
        self.max_ = root.val
        self.helper(root)
        return self.max_ - self.min_