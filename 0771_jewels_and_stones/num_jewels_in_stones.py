def num_jewels_in_stones(J: str, S: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    jewels = set(x for x in J)
    return sum(stone in jewels for stone in S)
