from typing import List


def shifting_letters(s: str, shifts: List[int]) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    res = ""
    for i in range(len(s) - 2, -1, -1):
        shifts[i] = shifts[i] + shifts[i + 1]
    for i, c in enumerate(s):
        res += shift_char_by_indexes(c, shifts[i])
    return res
    
def shift_char_by_indexes(char: str, num_of_indexes: int) -> str:
    a = ord('a')
    return chr((ord(char) - a + num_of_indexes) % 26 + a)