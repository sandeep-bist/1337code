class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.get_min())))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        """
        Gets minimum value in stack.
        """
        return self.stack[-1][1]
