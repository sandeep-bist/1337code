from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Time:    O(n * log(n) + 2**n)
    Space:   O(n**2)
    """
    res = []
    if not len(candidates):
        return res
    candidates.sort()
    dfs(candidates, [], 0, target, res)
    return res


def dfs(nums: List[int], sub: List[int], index: int, target: int,
        res: List[List[int]]):
    if target == 0:
        res.append(sub)
    for i in range(index, len(nums)):
        if nums[i] > target:
            break
        dfs(nums, sub + [nums[i]], i, target - nums[i], res)
