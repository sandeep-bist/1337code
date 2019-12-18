def roman_to_int(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer. Input is guaranteed to be
    within the range from 1 to 3999.
    """
    hash_map = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = prev = 0
    for i in s[::-1]:
        curr = hash_map[i]
        sum += curr if curr > prev else -curr
        prev = curr
    return sum


print(roman_to_int("MCMXCIV"))  # 1994
print(roman_to_int("IX"))  # 9
