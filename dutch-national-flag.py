# https://binarysearch.com/problems/List-Partitioning

# i, j, k. For an index p
# p < i: 0
# i <= p < j: 1
# j <= p <= k: unclassified
# k < p: 2
# we move j until it's > k. at that point there are no unclassified elements

class Solution:
    def solve(self, strs):
        i = 0
        j = 0
        k = len(strs)-1
        while j <= k:
            if strs[j] == 'red':
                strs[j], strs[i] = strs[i], strs[j]
                i += 1
                j += 1
            elif strs[j] == 'green':
                j += 1
            else:
                strs[j], strs[k] = strs[k], strs[j]
                k -= 1
            print(j, k, strs)
        return strs

strs = ["green", "blue", "red", "red"]

print(Solution().solve(strs))