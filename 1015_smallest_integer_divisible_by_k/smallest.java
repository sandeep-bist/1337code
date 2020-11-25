class Solution {
    // Time: O(n)
    // Space: O(1)
    public int smallestRepunitDivByK(int K) {
        int remainder = 0;
        for (int res = 1; res <= K; res++) {
            remainder = (remainder * 10 + 1) % K;
            if (remainder == 0) {
                return res;
            }
        }
        return -1;
    }
}