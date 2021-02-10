# https://binarysearch.com/problems/Common-Words

class Solution:
    def words(self, s):
        return set(w.lower() for w in s.split())

    def solve(self, s0, s1):
        return len(self.words(s0).intersection(self.words(s1)))