from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    """
    Time: O(n + m) where m is the number of edges
    Space: O(n)
    """
    if not node:
        return
    visited = {node: Node(node.val)}
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = Node(neighbor.val)
            visited.get(curr).neighbors.append(visited.get(neighbor))
    return visited.get(node)
