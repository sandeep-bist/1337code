class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False] * 100000

    def add(self, key: int) -> None:
        h = self.hashf(key)
        self.arr[h] = True

    def remove(self, key: int) -> None:
        h = self.hashf(key)
        self.arr[h] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = self.hashf(key)
        return self.arr[h]

    def hashf(self, key: int) -> int:
        h = 5381
        return ((h << 5) + h + key) % 100000


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
