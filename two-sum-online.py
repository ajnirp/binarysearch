from collections import Counter

class TwoSum:
    def __init__(self):
        self.storage = Counter()

    def add(self, val):
        self.storage[val] += 1

    def find(self, val):
        for elem in self.storage:
            if elem*2 == val:
                if self.storage[elem] == 2:
                    return True
            elif self.storage[val - elem] == 1:
                return True
        return False
