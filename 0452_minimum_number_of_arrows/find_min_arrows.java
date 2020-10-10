class Solution {
    // Time: O(n * log(n))
    // Space: O(1)
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int res = 1;
        int end = points[0][1];
        for (int[] point : points) {
            int x = point[0], y = point[1];
            if (x > end) {
                res++;
                end = y;
            }
        }
        return res;
    }
}