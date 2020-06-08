def is_power_of_two(n: int) -> bool:
    """
    Time: O(1)
    Space: O(1)
    """
    return not (n & (n - 1)) if n else 0
