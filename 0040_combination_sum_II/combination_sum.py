from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Time:    O(n * log(n) + 2**n)
    Space:   O(n**2)
    """
    res = []
    nums = sorted(candidates)
    dfs(nums, 0, [], target, res)
    return res


def dfs(nums: List[int], index: int, arr: List[int], target: int,
        res: List[List[int]]):
    if not target:
        res.append(arr)
        return
    for i in range(index, len(nums)):
        curr = nums[i]
        if i > index and curr == nums[i - 1]:
            continue
        if curr > target:
            break
        dfs(nums, i + 1, arr + [curr], target - curr, res)
