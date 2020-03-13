from typing import List, Tuple


def reorder_log_files(logs: List[str]) -> List[str]:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    def custom(log: str) -> Tuple[int, str]:
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    return sorted(logs, key=custom)
