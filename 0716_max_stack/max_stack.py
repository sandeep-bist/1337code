class MaxStack(list):
    def push(self, x: int) -> None:
        last = float("-inf") if not self else self[-1][1]
        self.append((x, max(x, last)))

    def pop(self) -> int:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def peekMax(self) -> int:
        return self[-1][1]

    def popMax(self) -> int:
        _max = self[-1][1]
        tmp = []
        while self[-1][0] != _max:
            tmp.append(self.pop())
        self.pop()
        while tmp:
            self.push(tmp.pop())
        return _max
