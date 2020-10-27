class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    // Time: O(n)
    // Space: O(1)
    public ListNode detectCycle(ListNode head) {
        ListNode t = head, h = head;
        while (t != null && t.next != null) {
            h = h.next;
            t = t.next.next;
            if (h == t) {
                t = head;
                while (t != h) {
                    t = t.next;
                    h = h.next;
                }
                return t;
            }
        }
        return null;
    }
}