def is_power_of_four(num: int) -> bool:
    """
    Time: O(1)
    Space: O(1)
    """
    return num and num & (num-1) == 0 and num.bit_length() & 1
