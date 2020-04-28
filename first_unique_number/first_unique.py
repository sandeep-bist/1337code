from collections import OrderedDict
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.set = set()
        self.od = OrderedDict()
        for n in nums:
            self.add(n)

    def show_first_unique(self) -> int:
        for k in self.od.keys():
            return k
        return -1

    def add(self, value: int) -> None:
        if value not in self.set:
            self.set.add(value)
            self.od[value] = 1
        else:
            self.od.pop(value, 1)
