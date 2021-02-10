# https://binarysearch.com/problems/Text-Editor

class Solution:
    def solve(self, s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '<':
                if i < len(s) - 1 and s[i+1] == '-':
                    if len(stack) > 0:
                        stack.pop()
                    i += 2
                    continue
            stack.append(s[i])
            i += 1
            continue
        return ''.join(stack)