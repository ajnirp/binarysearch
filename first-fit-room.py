# https://binarysearch.com/problems/First-Fit-Room

class Solution:
    def solve(self, rooms, target):
        for room in rooms:
            if room >= target:
                return room
        return -1