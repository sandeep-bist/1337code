class Solution {
    // Time: O(n)
    // Space: O(1)
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int pos = 0, curr = 0, total = 0;
        for (int i = 0; i < cost.length; i++) {
            curr += gas[i] - cost[i];
            total += gas[i] - cost[i];
            if (curr < 0) {
                curr = 0;
                pos = i + 1;
            }
        }
        return total >= 0 ? pos : -1;
    }
}