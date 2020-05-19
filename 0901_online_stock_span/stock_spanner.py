class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        """
        Time: O(q) where q is the number of calls to next()
        Space: O(q)
        """
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
