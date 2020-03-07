def roman_to_int(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    hash_map = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = prev = 0
    for i in s[::-1]:
        curr = hash_map[i]
        sum += -curr if prev > curr else curr
        prev = curr
    return sum
