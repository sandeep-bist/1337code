from collections import Counter


def balance_string_split(s: str) -> int:
    """
    Balanced strings are those who have equal quantity of 'L' and 'R'
    characters.
    Given a balanced string s split it in the maximum amount of balanced
    strings.
    Return the maximum amount of splitted balanced strings.
    """
    splits = 0
    c = Counter()
    for i in s:
        c[i] += 1
        if c['R'] == c['L']:
            splits += 1
            c.clear()
    return splits


print(balance_string_split("RLRRLLRLRL"))  # 4
print(balance_string_split("RLLLLRRRLR"))  # 3
print(balance_string_split("LLLLRRRR"))  # 1
