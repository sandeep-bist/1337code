from collections import defaultdict
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    res = []
    g = defaultdict(list)
    for dst, src in prerequisites:
        g[dst].append(src)
    visited = [0] * numCourses

    def dfs(node):
        if visited[node] == -1:  # cycle detected
            return False
        if visited[node] == 1:
            return True  # has been finished, and been added to res
        visited[node] = -1  # mark as visited
        for x in g[node]:
            if not dfs(x):
                return False
        visited[node] = 1  # mark as finished
        res.append(node)
        return True
    for x in range(numCourses):
        if not dfs(x):
            return []
    return res
