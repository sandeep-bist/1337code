import bisect
import itertools
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))

    def pick_index(self) -> int:
        """
        Time: O(log(n))
        Space:O(n)
        """
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
