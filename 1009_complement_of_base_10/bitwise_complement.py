def bitwise_complement(N: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    return (1 << N.bit_length()) - 1 - N if N else 1
