from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Time: O(n * 2**n)
    Space: O(n * 2**n)
    """
    res = []
    dfs(nums, 0, [], res)
    return res

def dfs(nums: List[int], index: int, path: List[int], res: List[List[int]]):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)