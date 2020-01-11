from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given a collection of candidate numbers (candidates) and a target number
    (target), find all unique combinations in candidates where the candidate
    numbers sums to target.
    Each number in candidates may only be used once in the combination.
    """
    res = []
    nums = sorted(candidates)
    dfs(nums, 0, [], target, res)
    return res


def dfs(nums: List[int], index: int, arr: List[int], target: int,
        res: List[List[int]]):
    """
    Depth-first search.
    """
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


arr = [10, 1, 2, 7, 6, 1, 5]
print(combination_sum(arr, 8))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
