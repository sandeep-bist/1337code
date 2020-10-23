from typing import List


def find132pattern(nums: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    n3 = float("-inf")
    for num in nums[::-1]:
        if n3 > num:
            return True
        while stack and stack[-1] < num:
            n3 = stack.pop()
        stack.append(num)
    return False
