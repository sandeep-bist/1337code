class ArrayReader:
    def get(self, index: int) -> int:
        pass


def search(reader, target):
    """
    Time: O(log(t)) where t is the index of the targer
    Space: O(1)
    """
    if reader.get(0) == target:
        return 0
    i, j = 0, 1
    while reader.get(j) <= target:
        i = j
        j <<= 1
    while i < j:
        mid = (i + j) // 2
        curr = reader.get(mid)
        if curr == target:
            return mid
        if curr > target:
            j = mid
        else:
            i = mid + 1
    return -1
