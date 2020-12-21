class Solution {
    // Time: O(n * log(n))
    // Space: O(n)
    public int smallestRangeII(int[] A, int K) {
        Arrays.sort(A);
        int min = A[0], max = A[A.length - 1];
        int res = max - min;
        for (int i = 0; i < A.length - 1; i++) {
            int curr = A[i], next = A[i + 1];
            res = Math.min(res, (Math.max(curr + K, max - K) - Math.min(next - K, min + K)));
        }
        return res;
    }
}