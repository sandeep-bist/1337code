public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    // Time: O(n**2)
    // Space: O(1)
    public ListNode insertionSortList(ListNode head) {
        ListNode sentinel = new ListNode();
        ListNode curr = head, left, right, next;
        while (curr != null) {
            left = sentinel;
            right = sentinel.next;
            while (right != null) {
                if (curr.val < right.val) {
                    break;
                }
                left = right;
                right = right.next;
            }
            next = curr.next;
            left.next = curr;
            curr.next = right;
            curr = next;
        }
        return sentinel.next;       
    }
}