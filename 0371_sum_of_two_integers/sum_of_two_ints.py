def get_sum(a: int, b: int) -> int:
    """
    Time: O(n)
    Space: O(1)   
    """
    # 32 bit integer max.
    MAX = 0x7FFFFFFF
    # Mask to get last 32 bits.
    mask = 0xFFFFFFFF
    while b:
        carry = (a & b)
        a = (a ^ b) & mask
        b = (carry << 1) & mask
    # (~) Converts big number into negative in Python.
    return a if a <= MAX else ~(a ^ mask)
