class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return

        res = TreeNode(root.val)
        if not root.children:
            return res

        res.left = self.encode(root.children[0])
        curr = res.left
        for child in root.children[1:]:
            curr.right = self.encode(child)
            curr = curr.right
        return res

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return

        res = Node(data.val, [])
        node = data.left
        while node:
            res.children.append(self.decode(node))
            node = node.right
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
