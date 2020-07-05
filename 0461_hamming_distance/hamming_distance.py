def hamming_distance(x: int, y: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    xor, res = x ^ y, 0
    while xor:
        res += 1
        xor &= (xor - 1)
    return res
