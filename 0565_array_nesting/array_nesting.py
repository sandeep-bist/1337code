from typing import List


def arrayNesting(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = 0
    for i in range(len(nums)):
        cnt = 0
        while nums[i] != -1:
            tmp = nums[i]
            nums[i] = -1
            cnt += 1
            i = tmp
        res = max(res, cnt)
    return res