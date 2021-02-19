# https://binarysearch.com/problems/Count-Contained-Intervals

class Solution:
    def solve(self, intervals):
        if len(intervals) == 0:
            return 0
        # sort by start, to tie-break, a later end should come first
        intervals.sort(key=lambda x: (x[0], -x[1]))
        upto = []
        min_start, max_end = intervals[0]
        for interval in intervals[:-1]:
            min_start = min(min_start, interval[0])
            max_end = max(max_end, interval[1])
            upto.append((min_start, max_end))
        result = 0
        for i, j in zip(intervals[1:], upto):
            min_, max_ = j
            start, end = i
            if min_ <= start and end <= max_:
                result += 1
        return result
