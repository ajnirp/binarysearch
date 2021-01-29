# https://binarysearch.com/problems/Pattern-to-Word-Bijection

import sys

def solve(s, p):
    s_words = s.split()
    if len(s_words) != len(p):
        return False
    f_map = {}
    r_map = {}
    for char, word in zip(p, s_words):
        if char in f_map:
            if f_map[char] != word:
                return False
            if f_map[char] in r_map:
                if r_map[f_map[char]] != char:
                    return False
            r_map[f_map[char]] = char
        else:
            f_map[char] = word
            if word in r_map and r_map[word] != char:
                return False
            r_map[word] = char
    return True

print(solve(sys.argv[1], sys.argv[2]))