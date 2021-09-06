from typing import List


def slowest_key(releaseTimes: List[int], keysPressed: str) -> str:
    """
    Timing: O(n)
    Space: O(1)
    """
    max_time, max_char = releaseTimes[0], keysPressed[0]
    for i in range(1, len(releaseTimes)):
        time, char = releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]
        if time > max_time or (time == max_time and char > max_char):
            max_time = time
            max_char = char
    return max_char