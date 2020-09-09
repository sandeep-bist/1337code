def compare_version(version1: str, version2: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    while v1 or v2:
        first = int(v1.pop(0)) if v1 else 0
        sec = int(v2.pop(0)) if v2 else 0
        if first > sec:
            return 1
        elif sec > first:
            return -1
    return 0
