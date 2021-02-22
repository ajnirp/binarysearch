# https://binarysearch.com/problems/Removing-Parentheses

# just run the stack algorithm, with the modification that the return-false case
# (i.e. you see close and you don't see open at the top of the stack) is replaced
# by a simple append. then return the number of left-over elements i.e. stack len
# to reconstruct the string, you should also track indices

# from leetcode editorial:
# Remove a ")" if it is encountered when stack was already empty (prevent negative balance).
# Remove a "(" if it is left on stack at end (prevent non-zero final balance).


class Solution:
    def solve(self, s):
        stack = []
        for c in s:
            if c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)