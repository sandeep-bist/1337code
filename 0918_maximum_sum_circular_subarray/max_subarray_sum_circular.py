from typing import List


def max_subarray_sum_circular(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    max_curr = max_so_far = float("-inf")
    min_curr = min_so_far = total = 0
    for a in A:
        max_curr = max(max_curr + a, a)
        max_so_far = max(max_so_far, max_curr)
        min_curr = min(min_curr + a, a)
        min_so_far = min(min_so_far, min_curr)
        total += a
    return max(max_so_far, total - min_so_far) if max_so_far > 0 else max_so_far
