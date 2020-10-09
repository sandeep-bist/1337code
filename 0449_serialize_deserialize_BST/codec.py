from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        return self.inorder("", root)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        node_list = data.split(",")
        return self.build(deque(node_list))

    def inorder(self, output: str, node: TreeNode) -> str:
        """
        Inorder traversal and serialization.
        """
        if not node:
            output += "None,"
        else:
            output += str(node.val) + ","
            output = self.inorder(output, node.left)
            output = self.inorder(output, node.right)
        return output

    def build(self, node_list: List[TreeNode]) -> TreeNode:
        """
        Builds out BST from list.
        """
        if node_list[0] == "None":
            node_list.popleft()
            return
        root = TreeNode(node_list.popleft())
        root.left = self.build(node_list)
        root.right = self.build(node_list)
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
