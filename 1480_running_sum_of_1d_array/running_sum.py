from typing import List


def runningSum(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    tmp = 0
    for n in nums:
        tmp += n
        res.append(tmp)
    return res