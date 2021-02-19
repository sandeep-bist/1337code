class Solution {
    // Time: O(n)
    // Space: O(1)
    public int maxArea(int[] height) {
        int max = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            int min = Math.min(height[i], height[j]);
            max = Math.max(max, (j - i) * min);
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return max;
    }
}