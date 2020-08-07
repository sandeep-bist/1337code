from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode) -> List[List[int]]:
    """
    Time: O(n**2 * log(n))
    Space: O(n)
    """
    g = collections.defaultdict(list)
    queue = [(root, 0)]
    while queue:
        tmp = []
        d = collections.defaultdict(list)
        for node, s in queue:
            d[s].append(node.val)
            if node.left:
                tmp += (node.left, s-1),
            if node.right:
                tmp += (node.right, s+1),
        print(f"{d=}")
        for i in d:
            g[i].extend(sorted(d[i]))
        queue = tmp
        print(f"{g=}")
    return [g[i] for i in sorted(g)]
