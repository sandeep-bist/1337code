from collections import Counter
from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    Time: O(∑(N,k=1)) P(N,k))
    Space: O(n)
    """
    results = []
    def backtrack(comb, counter):
        if len(comb) == len(nums):
            results.append(list(comb))
            return
        for num in counter:
            if counter[num] > 0:
                comb.append(num)
                counter[num] -= 1
                backtrack(comb, counter)
                comb.pop()
                counter[num] += 1
    backtrack([], Counter(nums))
    return results