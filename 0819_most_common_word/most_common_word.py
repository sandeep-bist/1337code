from collections import Counter
import re
from typing import List


def most_common_word(p: str, banned: List[str]):
    """
    Time: O(m + n)
    Space: O(m + n)
    """
    s = set(banned)
    words = re.findall(r'\w+', p.lower())  # list of lower case words
    return Counter(w for w in words if w not in s).most_common(1)[0][0]
