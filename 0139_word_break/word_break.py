from collections import deque
from typing import List


def word_break(s: str, wordDict: List[str]) -> bool:
    """
    Time: O(n**2)
    Space: O(n)
    """
    q = deque([s])
    seen = set()
    while q:
        curr = q.popleft()
        for word in wordDict:
            if curr.startswith(word):
                rest = curr[len(word):]
                if rest == "":
                    return True
                if rest not in seen:
                    seen.add(rest)
                    q.append(rest)
    return False
