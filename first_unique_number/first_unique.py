from collections import OrderedDict
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        """
        Space: O(n)
        """
        self.set = set()
        self.od = OrderedDict()
        for n in nums:
            self.add(n)

    def show_first_unique(self) -> int:
        """
        Time: O(1)
        """
        for k in self.od.keys():
            return k
        return -1

    def add(self, value: int) -> None:
        """
        Time: O(1)
        """
        if value not in self.set:
            self.set.add(value)
            self.od[value] = 1
        else:
            self.od.pop(value, 1)
