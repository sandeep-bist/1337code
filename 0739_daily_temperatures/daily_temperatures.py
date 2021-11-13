from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = [0] * len(temperatures)
    stack = []
    for curr_day, curr_tmp in enumerate(temperatures):
        while stack and curr_tmp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            res[prev_day] = curr_day - prev_day
        stack.append(curr_day)
    return res