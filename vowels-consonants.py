# https://binarysearch.com/problems/Vowels-and-Consonants-Sort

class Solution:
    def solve(self, s):
        vowels = []
        consonants = []
        for c in s:
            if c in 'aeiou':
                vowels.append(c)
            else:
                consonants.append(c)
        return ''.join(sorted(vowels)) + ''.join(sorted(consonants))
