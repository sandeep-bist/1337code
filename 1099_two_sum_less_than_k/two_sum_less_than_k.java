class Solution {
    // Time: O(n * log(n))
    // Space: O(1)
    public int twoSumLessThanK(int[] A, int K) {
        int res = -1;
        Arrays.sort(A);
        int i = 0, j = A.length - 1;
        while (i < j) {
            if (A[i] + A[j] < K) {
                res = Math.max(res, A[i] + A[j]);
                i++;
            } else {
                j--;
            }
        }
        return res;
    }
}