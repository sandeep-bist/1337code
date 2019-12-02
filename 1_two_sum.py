def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    """
    map = {}
    for i, e in enumerate(nums):
        compliment = target - e
        if compliment in map:
            return [map[compliment], i]
        else:
            map[e] = i
    return []


print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
