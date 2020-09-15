class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};

class Solution {
    // Time: O(log(n))
    // Space: O(1)
    public Node inorderSuccessor(Node node) {
        Node curr = node;
        if (curr.right != null) {
            curr = curr.right;
            while (curr.left != null) {
                curr = curr.left;
            }
            return curr;
        }
        while (curr.parent != null) {
            curr = curr.parent;
            if (curr.val > node.val) {
                return curr;
            }
        }
        return null;
    }
}