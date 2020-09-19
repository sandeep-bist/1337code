from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    """
    Time: O(1)
    Space: O(1)
    """
    nums = "123456789"
    i, j = len(str(low)), len(str(high))
    res = []
    for size in range(i, j + 1):
        for start in range(10 - size):
            num = int(nums[start: start + size])
            if high >= num >= low:
                res.append(num)
    return res
