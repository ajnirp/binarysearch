# https://binarysearch.com/problems/Monotonous-String-Groups

# the state to be maintained is:
# how many groups we've seen
# are we increasing, decreasing or not-sure (key insight)

class Solution:
    def solve(self, s):
        if len(s) == 0:
            return 0
        state = 'uncertain'
        stack = [s[0]]
        groups = 1
        for c in s[1:]:
            if state == 'uncertain':
                if c > stack[-1]:
                    state = 'ascending'
                    stack.append(c)
                elif c < stack[-1]:
                    state = 'descending'
                    stack.append(c)
                else:
                    stack.append(c)
            elif state == 'ascending':
                if c > stack[-1]:
                    stack.append(c)
                elif c < stack[-1]:
                    state = 'uncertain'
                    groups += 1
                    stack = [c]
                else:
                    stack.append(c)
            elif state == 'descending':
                if c > stack[-1]:
                    state = 'uncertain'
                    groups += 1
                    stack = [c]
                elif c < stack[-1]:
                    stack.append(c)
                else:
                    stack.append(c)
        return groups