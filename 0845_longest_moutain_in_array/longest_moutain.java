class Solution {
    // Time: O(n)
    // Space: O(1)
    public int longestMountain(int[] A) {
        int N = A.length;
        int res = 0, base = 0;
        while (base < N) {
            int end = base;
            if (end + 1 < N && A[end] < A[end + 1]) {
                while (end + 1 < N && A[end] < A[end + 1]) {
                    end++;
                }
                if (end + 1 < N && A[end] > A[end + 1]) {
                    while (end + 1 < N && A[end] > A[end + 1]) {
                        end++;
                    }
                    res = Math.max(res, end - base + 1);
                }
            }
            base = Math.max(end, base + 1);
        }
        return ans;
    }
}