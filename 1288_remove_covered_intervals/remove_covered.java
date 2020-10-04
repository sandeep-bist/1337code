import java.util.Arrays;

class Solution {
    // Time: O(n * log(n))
    // Space: O(1)
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int res = 0, left = -1, right = -1;
        for (int[] interval : intervals) {
            if (interval[0] > left && interval[1] > right) {
                res++;
                left = interval[0];
            }
            right = Math.max(right, interval[1]);
        }
        return res;
    }
}