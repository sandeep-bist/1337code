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
    // Time: O(n * log(n))
    // Space: O(1)
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode mid = getMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);

    }

    private ListNode getMid(ListNode head) {
        ListNode midPrev = null;
        while (head != null && head.next != null) {
            midPrev = (midPrev == null) ? head : midPrev.next;
            head = head.next.next;
        }
        ListNode mid = midPrev.next;
        midPrev.next = null;
        return mid;
    }

    private ListNode merge(ListNode first, ListNode sec) {
        ListNode sentinel = new ListNode();
        ListNode tail = sentinel;
        while (first != null && sec != null) {
            if (first.val < sec.val) {
                tail.next = first;
                first = first.next;
            } else {
                tail.next = sec;
                sec = sec.next;
            }
            tail = tail.next;
        }
        tail.next = (first != null) ? first : sec;
        return sentinel.next;
    }
}