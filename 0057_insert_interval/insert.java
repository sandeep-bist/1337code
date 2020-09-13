import java.util.List;
import java.util.ArrayList;

class Solution {
    // Time: O(n)
    // Space: O(n)
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int i = 0, n = intervals.length;
        int start = newInterval[0], end = newInterval[1];
        while (i < n && intervals[i][1] < start) {
            res.add(new int[] { intervals[i][0], intervals[i][1] });
            i++;
        }
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        res.add(new int[] { start, end });
        while (i < n && intervals[i][0] > end) {
            res.add(new int[] { intervals[i][0], intervals[i][1] });
            i++;
        }
        return res.toArray(new int[res.size()][2]);
    }
}