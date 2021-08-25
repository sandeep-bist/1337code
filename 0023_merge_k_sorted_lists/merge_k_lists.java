 public class Solution {
     // Time: O(k * n * log(n))
     // Space: O(k * n)
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
            
        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, (a,b) -> a.val - b.val);
            
        ListNode sentinel = new ListNode(0);
        ListNode tail = sentinel;
            
        for (ListNode node : lists) {
            if (node != null) {
                queue.add(node);
            }
        }
        while (!queue.isEmpty()) {
            tail.next = queue.poll();
            tail = tail.next;
            if (tail.next != null) {
                queue.add(tail.next);
            }
        }
        return sentinel.next;
    }
}

    
