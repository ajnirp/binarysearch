# https://binarysearch.com/problems/Linked-List-Jumps

# note: not optimal since it ignores the fact that all values are positive,
# meaning we can just skip ahead

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node is None:
            return None
        nodes = {}
        n = 0
        orig_head = node
        head = node
        while head:
            nodes[n] = head
            head = head.next
            n += 1
        for i in range(n):
            val = nodes[i].val
            if i + val not in nodes:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i + val]
        return orig_head
