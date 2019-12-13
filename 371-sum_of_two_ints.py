def getSum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers a and b, but you are not allowed to use
    the operator + and -.     
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


print(getSum(-12, -8))  # -20
print(getSum(1, 2))  # 3
