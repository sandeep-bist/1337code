class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    return preorder(root, 0, target)


def preorder(node: TreeNode, curr_sum: int, target: int, cache=defaultdict(int)):
    if not node:
        return 0
    curr_sum += node.val
    res = cache[curr_sum - target]
    if curr_sum == target:
        res += 1
    cache[curr_sum] += 1
    res += preorder(node.left, curr_sum, target, cache) + \
        preorder(node.right, curr_sum, target, cache)
    cache[curr_sum] -= 1
    return res
