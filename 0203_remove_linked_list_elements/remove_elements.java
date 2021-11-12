public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    // Time: O(n)
    // Space: O(1)
    public ListNode removeElements(ListNode head, int val) {
        ListNode sentinel = new ListNode(-1);
        ListNode curr = sentinel;
        while (head != null) {
            if (head.val != val) {
                curr.next = head;
                curr = curr.next;
            }
            head = head.next;
        }
        curr.next = null;
        return sentinel.next;
    }
}