# https://binarysearch.com/problems/Linked-List-to-Integer

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node):
        result = 0
        while node:
            result += node.val
            result <<= 1
            node = node.next
        return result >> 1 # undo the extra shift before returning
        