from typing import List


def compress(self, chars: List[str]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    read = write = 0
    while read < len(chars):
        curr = chars[read]
        count = 0
        while read < len(chars) and curr == chars[read]:
            read += 1
            count += 1
        chars[write] = curr
        write += 1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
    return write
