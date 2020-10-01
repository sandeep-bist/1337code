class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxDistance(List<List<Integer>> arrays) {
        int res = 0, n = arrays.get(0).size() - 1;
        int min = arrays.get(0).get(0);
        int max = arrays.get(0).get(n);
        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> arr = arrays.get(i);
            n = arr.size() - 1;
            int tmp = Math.max(arr.get(n) - min, max - arr.get(0));
            res = Math.max(res, tmp);
            min = Math.min(min, arr.get(0));
            max = Math.max(max, arr.get(n));
        }
        return res;
    }
}