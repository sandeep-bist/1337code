class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxTurbulenceSize(int[] arr) {
        int res = 1, dec = 1, inc = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1]) {
                inc = dec + 1;
                dec = 1;
            } else if (arr[i - 1] > arr[i]) {
                dec = inc + 1;
                inc = 1;
            } else {
                dec = 1;
                inc = 1;
            }
            res = Math.max(res, Math.max(inc, dec));
        }
        return res;
    }
}