class Solution {
    // Time: O(n)
    // Space: O(1)
    public int jump(int[] nums) {
        int res = 0, currFarthest = 0, currEnd = 0;
        int goal = nums.length - 1;
        for (int i = 0; i < goal; i++) {
            currFarthest = Math.max(currFarthest, nums[i] + i);
            if (i == currEnd) {
                res++;
                currEnd = currFarthest;
                if (currFarthest >= goal) {
                    break;
                }
            }
        }
        return res;
    }
}