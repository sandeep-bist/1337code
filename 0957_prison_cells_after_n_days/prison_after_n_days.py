from typing import List


def prison_after_n_days_math(cells: List[int], N: int) -> List[int]:
    """
    Time: O(n % 14)
    Space: O(n % 14)
    """
    for i in range((N-1) % 14 + 1):
        cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
    return cells


def prison_after_n_days(cells: List[int], N: int) -> List[int]:
    seen = {str(cells): N}
    while N:
        seen.setdefault(str(cells), N)
        N -= 1
        cells = [0] + [cells[i - 1] ^ cells[i + 1]
                       ^ 1 for i in range(1, 7)] + [0]
        if str(cells) in seen:
            N %= seen[str(cells)] - N
    return cells
