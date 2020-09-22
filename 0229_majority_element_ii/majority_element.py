from typing import List


def majority_element(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    res = []
    if not nums:
        return res
    c1 = c2 = 0
    num1 = num2 = nums[0]
    n = len(nums)
    for num in nums:
        if num == num1:
            c1 += 1
        elif num == num2:
            c2 += 1
        elif not c1:
            num1 = num
            c1 = 1
        elif not c2:
            num2 = num
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    c1 = c2 = 0
    for num in nums:
        if num == num1:
            c1 += 1
        elif num == num2:
            c2 += 1
    if c1 > n // 3:
        res.append(num1)
    if c2 > n // 3:
        res.append(num2)
    return res
