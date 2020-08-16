// Time: O(n)
// Space: O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            int difference = target - curr;
            if (hashMap.containsKey(difference))
                return new int[]{i, hashMap.get(difference)};
            hashMap.put(curr, i); 
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}