def add_binary(a: str, b: str) -> str:
    """
    Time: O(n + m)
    Space: O(n + m)
    """
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary_alt(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]


