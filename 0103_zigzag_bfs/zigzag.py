from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res, tmp, q = [], [], deque([root])
    flag = 1
    while q:
        for i in range(len(q)):
            node = q.popleft()
            tmp += [node.val]
            if node.left:
                q += [node.left]
            if node.right:
                q += [node.right]
        res += [tmp[::flag]]
        tmp = []
        flag *= -1
    return res
