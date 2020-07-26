def add_digits(num: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    return 1 + (num - 1) % 9 if num else 0
