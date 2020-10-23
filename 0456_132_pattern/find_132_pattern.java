import java.util.Stack;

class Solution {
    // Time: O(n)
    // Space: O(n)
    public boolean find132pattern(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int n3 = Integer.MIN_VALUE;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (n3 > nums[i]) {
                return true;
            }
            while (!stack.isEmpty() && stack.peek() < nums[i]) {
                n3 = stack.pop();
            }
            stack.add(nums[i]);
        }
        return false;

    }
}