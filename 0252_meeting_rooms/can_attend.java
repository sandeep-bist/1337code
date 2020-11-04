class Solution {
    // Time: O(n * log(n))
    // Space: O(1)
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                return false;
            }
            end = intervals[i][1];
        }
        return true;
    }
}