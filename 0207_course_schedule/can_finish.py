from collections import defaultdict
from typing import List


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Time complexity: O(n**2 + e) where e is the number of edges
    Space complexity: O(n + e)
    """
    graph = defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)
    status = [0] * numCourses

    def dfs(i):
        if status[i] in {1, -1}:
            return status[i] == 1
        status[i] = -1
        if any(not dfs(j) for j in graph[i]):
            return False
        status[i] = 1
        return True
    return all(dfs(i) for i in range(numCourses))
