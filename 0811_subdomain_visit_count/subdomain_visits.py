from collections import Counter
from typing import List


def subdomainVisits(cpdomains: List[str]) -> List[str]:
    """
    Time: O(n)
    Space: O(n)
    """
    visited = Counter()
    for cpdomain in cpdomains:
        visits, domain = cpdomain.split(" ")
        dots = domain.count(".")
        while True:
            visited[domain] += int(visits)
            if dots:
                domain = domain.split(".", 1)[1]
            else:
                break
            dots -= 1
    return [f"{v} {k}" for k, v in visited.items()]
