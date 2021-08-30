class Solution {
    // Time: O(n)
    // Space: O(n)
    public int minPatches(int[] nums, int n) {
        long missing = 1;
        int i = 0;
        ArrayList<Long> patches = new ArrayList<>();
        while (missing <= n) {
            if (i < nums.length && nums[i] <= missing) {
                missing += nums[i++];
            } else {
                patches.add(missing);
                missing += missing;
            }
        }
        return patches.size();
    }
}