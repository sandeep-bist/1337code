from typing import List, Dict


def find_repeat_dna(s: str) -> List[str]:
    """
    Time: O(n)
    Space: O(n)
    """
    SUBSTR_SIZE = 10
    size = len(s)
    if SUBSTR_SIZE >= size:
        return []
    m = create_map(s)
    num_chars = len(m)
    base = (num_chars)**(SUBSTR_SIZE)
    seen, res = set(), set()
    nums = convert_to_num_list(s, m)
    h = 0
    for i in range(size - SUBSTR_SIZE + 1):
        if not i:
            # first sequence
            for i in range(SUBSTR_SIZE):
                h = h * num_chars + int(nums[i])
        else:
            # subtract previous number * base
            p = int(nums[i - 1]) * base
            # add next number
            n = int(nums[i + SUBSTR_SIZE - 1])
            h = (h * num_chars) - p + n
        if h in seen:
            res.add(s[i: i + SUBSTR_SIZE])
        seen.add(h)
    return list(res)


def create_map(s: str):
    s = set(c for c in s)
    return {y: x for x, y in enumerate(s)}


def convert_to_num_list(s: str, m: Dict[str, int]):
    return [m.get(c) for c in s]
