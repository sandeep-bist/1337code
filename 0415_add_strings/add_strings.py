from typing import List


def add_strings(num1: str, num2: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    nums1, nums2 = list(num1), list(num2)
    carry, res = 0, []
    while nums1 or nums2 or carry:
        first = get_last_digit(nums1) if nums1 else 0
        second = get_last_digit(nums1) if nums2 else 0
        carry, remain = divmod(first + second + carry, 10)
        res.append(remain)
    return "".join(str(x) for x in res)[::-1]


def get_last_digit(arr: List[str]) -> int:
    return ord(arr.pop()) - ord("0")
