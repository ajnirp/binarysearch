# https://binarysearch.com/problems/Task-Hare

class Solution:
    def solve(self, tasks, people):
        tasks.sort(reverse=True)
        people.sort(reverse=True)
        t, p = 0, 0
        doable = 0
        while t < len(tasks) and p < len(people):
            if tasks[t] > people[p]:
                t += 1
            else:
                t += 1
                p += 1
                doable += 1
        return doable

print(Solution().solve([3, 2, 9, 13], [10, 5, 2, 1]))