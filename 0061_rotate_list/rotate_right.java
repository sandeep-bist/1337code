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

class Solution {
    // Time: O(n)
    // Space: O(1)
    public ListNode rotateRight(ListNode head, int k) {
        if (k == 0 || head == null || head.next == null) {
            return head;
        }
        int size = 1;
        ListNode curr = head;
        while (curr.next != null) {
            curr = curr.next;
            size++;
        }
        curr.next = head;
        int rotations = k % size;
        ListNode end = head, start = head;
        for (int i = 0; i < size - rotations - 1; i++) {
            end = end.next;
        }
        start = end.next;
        end.next = null;
        return start;
    }
}