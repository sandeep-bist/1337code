class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        """
        Time: O(2**n * n)
        Space: O(k * C**k)
        """
        self.combinations = []
        n, k = len(characters), combinationLength
        for bitmask in range(1 << n):
            if bin(bitmask).count('1') == k:
                curr = [characters[j]
                        for j in range(n) if bitmask & (1 << n - j - 1)]
                self.combinations.append(''.join(curr))

    def next(self) -> str:
        """
        Time: O(1)
        """
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
