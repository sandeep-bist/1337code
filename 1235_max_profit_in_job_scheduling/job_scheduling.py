from typing import List
from bisect import bisect


def job_scheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    """
    Time: O(n log n) + O(n log n)
    Space: O(n)
    """
    jobs = sort_by_end_time(startTime, endTime, profit)
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = find_insert_idx(dp, s)
        curr_profit = dp[i][1] + p
        if curr_profit > dp[-1][1]:
            dp.append([e, curr_profit])
    return dp[-1][1]

def sort_by_end_time(start: int, end: int, profit: int) -> List[int]:
    return sorted(zip(start, end, profit), key=lambda v: v[1])

def find_insert_idx(arr: List[int], start: int) -> int:
    return bisect(arr, [start + 1]) - 1