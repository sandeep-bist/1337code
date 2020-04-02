from typing import List


def valid_utf8(data: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    num_bytes = 0
    for n in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & n:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if n >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0


def valid_utf8_alt(self, data: List[int]) -> bool:
    count = 0
    for n in data:
        if not count:
            if n >> 5 == 0b110:
                count = 1
            elif n >> 4 == 0b1110:
                count = 2
            elif n >> 3 == 0b11110:
                count = 3
            elif n >> 7:
                return False
        else:
            if n >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
