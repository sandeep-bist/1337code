def reverse(x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    """
    s = [1, -1][x < 0]
    res = s * int(str(abs(x))[::-1])
    return res if res.bit_length() < 32 else 0


print(reverse(123))  # 321
print(reverse(120))  # 21
print(reverse(-914))  # -419
