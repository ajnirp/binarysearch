# https://binarysearch.com/problems/Left-Side-View-of-a-Tree

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root):
        curr = [root]
        result = []
        while len(curr) > 0:
            result.append(curr[0].val)
            next_ = []
            for node in curr:
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            if len(next_) == 0:
                break
            curr = next_
        return result

t = Tree(0, Tree(5), Tree(2, None, Tree(1)))

print(Solution().solve(t))