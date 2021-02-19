class Solution {
    // Time: O(n)
    // Space: O(1)
    public int numberOfArithmeticSlices(int[] A) {
        int res = 0, curr = 0;
        for (int i = 2; i < A.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                curr += 1;
                res += curr;
            } else {
                curr = 0;
            }
        }
        return res;
    }
}