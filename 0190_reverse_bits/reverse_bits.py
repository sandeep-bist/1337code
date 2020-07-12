def reverse_bits(n: int) -> int:
    res, j = 0, 0
    for i in range(31, -1, -1):
        curr = (n >> i) & 1
        res |= (curr << j)
        j += 1
    return res
