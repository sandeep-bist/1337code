class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def subtreeWithAllDeepest(root: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    depth = {None: -1}
    def dfs(node, parent = None):
        if node:
            depth[node] = depth[parent] + 1
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)

    max_depth = max(depth.values())

    def answer(node: TreeNode) -> TreeNode:
        if not node or depth.get(node, None) == max_depth:
            return node
        L, R = answer(node.left), answer(node.right)
        return node if L and R else L or R

    return answer(root)