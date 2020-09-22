import java.util.List;
import java.util.ArrayList;

class Solution {
    // Time: O(n)
    // Space: O(1)
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums.length == 0) {
            return res;
        }
        int num1 = nums[0], num2 = nums[0];
        int c1 = 0, c2 = 0, len = nums.length;
        for (int i = 0; i < len; i++) {
            if (nums[i] == num1) {
                c1++;
            } else if (nums[i] == num2) {
                c2++;
            } else if (c1 == 0) {
                num1 = nums[i];
                c1 = 1;
            } else if (c2 == 0) {
                num2 = nums[i];
                c2 = 1;
            } else {
                c1--;
                c2--;
            }
        }
        c1 = 0;
        c2 = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] == num1) {
                c1++;
            } else if (nums[i] == num2) {
                c2++;
            }
        }
        if (c1 > len / 3) {
            res.add(num1);
        }
        if (c2 > len / 3) {
            res.add(num2);
        }
        return res;
    }
}