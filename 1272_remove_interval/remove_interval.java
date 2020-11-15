class Solution {
    // Time: O(n)
    // Space: O(n)
    public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
        List<List<Integer>> res = new ArrayList<>();
        int a = toBeRemoved[0], b = toBeRemoved[1];
        for (int[] interval: intervals) {
            int x = interval[0], y = interval[1];
            if (x < a) {
                res.add(Arrays.asList(x, Math.min(y, a)));
            }
            if (y > b) {
                res.add(Arrays.asList(Math.max(x, b), y));
            }
        }
        return res;
    }
}