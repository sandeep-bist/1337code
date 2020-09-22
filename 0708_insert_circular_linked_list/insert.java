/* Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    // Time: O(n)
    // Space: O(1)
    public Node insert(Node head, int insertVal) {
        Node node = new Node(insertVal);
        if (head == null) {
            node.next = node;
            return node;
        }
        Node prev = head, curr = head;
        while (true) {
            prev = curr;
            curr = curr.next;
            if (insertVal >= prev.val && insertVal <= curr.val) {
                break;
            }
            if (prev.val > curr.val) {
                if (insertVal >= prev.val || insertVal <= curr.val) {
                    break;
                }
            }
            if (curr == head) {
                break;
            }
        }
        prev.next = node;
        node.next = curr;
        return head;
    }
}