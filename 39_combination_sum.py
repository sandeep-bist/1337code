from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a
    target number (target), find all unique combinations in candidates where
    the candidate numbers sums to target.
    The same repeated number may be chosen from candidates unlimited number
    of times.
    """
    res = []
    if not len(candidates):
        return res
    candidates.sort()
    dfs(candidates, [], 0, target, res)
    return res


def dfs(nums: List[int], sub: List[int], index: int, target: int, res: List[List[int]]):
    """
    Depth-first search.
    """
    if target == 0:
        res.append(sub)
    for i in range(index, len(nums)):
        if nums[i] > target:
            break
        dfs(nums, sub + [nums[i]], i, target - nums[i], res)


arr = [2, 3, 6, 7]
print(combination_sum(arr, 7))  # [[2, 2, 3], [7]]
