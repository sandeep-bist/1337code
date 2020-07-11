from collections import deque
from typing import Dict, List


def width_of_binary_tree_bfs(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return 0
    res = 0
    q = deque()
    q.append((root, 0))
    while q:
        size = len(q)
        _, first_index = q[0]
        for __ in range(size):
            node, last_index = q.popleft()
            if node.left:
                q.append((node.left, 2 * last_index))
            if node.right:
                q.append((node.right, 2 * last_index + 1))
        res = max(res, last_index - first_index + 1)
    return


def width_of_binary_tree(root: TreeNode) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    ht = {}
    res = [0]
    dfs(root, 0, 0, ht, res)
    return res[0]


def dfs(node: TreeNode, depth: int, index: int, ht: Dict[int, int], res: List[int]):
    if not node:
        return
    if depth not in ht:
        ht[depth] = index
    res[0] = max(res[0], index - ht[depth] + 1)
    dfs(node.left, depth+1, 2*index, ht, res)
    dfs(node.right, depth+1, 2*index + 1, ht, res)
