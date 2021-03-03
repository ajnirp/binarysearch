# https://binarysearch.com/problems/Univalue-Tree-Count

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, node):
        recurs = []
        if node.left is not None:
            recurs.append(self.helper(node.left))
        if node.right is not None:
            recurs.append(self.helper(node.right))
        if all(recur == node.val for recur in recurs):
            self.result += 1
            return node.val
        return None # dummy value that no node ever takes on

    def solve(self, root):
        self.result = 0
        self.helper(root)
        return self.result

t = Tree(0,
         Tree(0, None, Tree(1)),
         Tree(0))
print(Solution().solve(t))