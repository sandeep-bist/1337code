// Time: O(n)
// Space: O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            int compliment = target - curr;
            if (map.containsKey(compliment))
                return new int[]{i, map.get(compliment)};
            map.put(curr, i); 
        }
        return new int[]{};
    }
}