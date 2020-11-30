from typing import List


def canReach(arr: List[int], start: int) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        arr[start] = -arr[start]
        return (canReach(arr, start+arr[start]) or
                canReach(arr, start-arr[start]))
    return False