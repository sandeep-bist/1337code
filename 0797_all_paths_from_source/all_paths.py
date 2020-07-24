from typing import List


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    """
    Time: O(2**n * n)
    Space: O(2**n * n)
    """
    target = len(graph) - 1

    @lru_cache(maxsize=None)
    def dp(currNode):
        if curr == target:
            return [[target]]
        res = []
        for next_node in graph[curr]:
            for path in dp(next_node):
                res.append([curr] + path)
        return res
    return dp(0)
