from bisect import insort


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        Time: O(log(n))
        """
        insort(self.arr, number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        Time: O(n)
        """
        i, j = 0, len(self.arr) - 1
        while i < j:
            s = self.arr[i] + self.arr[j]
            if s == value:
                return True
            if s > value:
                j -= 1
            else:
                i += 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
