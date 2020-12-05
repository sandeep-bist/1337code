from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= n