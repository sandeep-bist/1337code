from collections import deque


class RecentCounter:

    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        self.window.append(t)
        while self.window:
            if t - 3000 > self.window[0]:
                self.window.popleft()
            else:
                break
        return len(self.window)
