public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

// Time: O(n)
// Space: O(1)
class Solution {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }
        ListNode mid = findMiddleNode(head);
        ListNode midHead = reverseList(mid);
        mergeLists(head, midHead);
    }

    private ListNode findMiddleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head, tmp;
        while (curr != null) {
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        return prev;
    }

    private void mergeLists(ListNode head1, ListNode head2) {
        ListNode first = head1, second = head2, tmp;
        while (second.next != null) {
            tmp = first.next;
            first.next = second;
            first = tmp;
            tmp = second.next;
            second.next = first;
            second = tmp;
        }
    }
}