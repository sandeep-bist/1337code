from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.max_size = size
        self.total = 0

    def next(self, val: int) -> float:
        """
        Time: O(1)
        Space: O(1)
        """
        if len(self.q) >= self.max_size:
            self.total -= self.q.popleft()
        self.q.append(val)
        self.total += val
        return self.total / len(self.q)
