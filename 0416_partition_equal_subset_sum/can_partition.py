from typing import List


def canPartition(nums: List[int]) -> bool:
    """
    Time: O(n * m) where m is the subSetSum and n is the number of array elements
    Space: O(m)
    """
    if not nums:
        return False
    total = sum(x for x in nums)
    if total & 1:
        return False
    subset_sum = total // 2
    dp = [False] * (subset_sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(subset_sum, num - 1, -1):
            dp[i] |= dp[i - num]
    return dp[subset_sum]