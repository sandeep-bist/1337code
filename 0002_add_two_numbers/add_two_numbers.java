public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbersHelper(l1, l2, 0);
    }
    
    public ListNode addTwoNumbersHelper(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        }
        int tmp = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
        ListNode node = new ListNode(tmp % 10);
        node.next = addTwoNumbersHelper(
            (l1 != null ? l1.next : null),
            (l2 != null ? l2.next : null),
            (tmp > 9 ? 1 : 0)
        );
        return node;
    }
}