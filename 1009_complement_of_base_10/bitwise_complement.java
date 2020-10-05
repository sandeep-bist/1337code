class Solution {
    // Time: O(1)
    // Space: O(1)
    public int bitwiseComplement(int N) {
        return N == 0 ? 1 : (Integer.highestOneBit(N) << 1) - N - 1;
    }
}