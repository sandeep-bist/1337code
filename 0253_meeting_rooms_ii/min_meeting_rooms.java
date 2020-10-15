import java.util.PriorityQueue;

class Solution {
    // Time: O(n * log(n))
    // Space: O(n)
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> heap = new PriorityQueue<>(intervals.length, (a, b) -> a - b);
        heap.offer(intervals[0][1]);
        for (int i = 1; i < intervals.length; i++) {
            if (heap.peek() <= intervals[i][0]) {
                heap.poll();
            }
            heap.add(intervals[i][1]);
        }
        return heap.size();
    }
}