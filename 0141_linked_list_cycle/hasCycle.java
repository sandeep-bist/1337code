class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode tort = head, hare = head;
        while (hare.next != null && hare.next.next != null) {
            hare = hare.next.next;
            tort = tort.next;
            if (hare == tort) {
                return true;
            }
        }
        return false;
    }
}