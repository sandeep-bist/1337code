import java.util.List;
import java.util.ArrayList;

class Solution {
    // Time: O(n)
    // Space: O(n)
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int tmp = i;
            while (i + 1 < nums.length && nums[i + 1] - nums[i] == 1) {
                i++;
            }
            if (tmp != i) {
                res.add(nums[tmp] + "->" + nums[i]);
            } else {
                res.add(nums[i] + "");
            }
        }
        return res;
    }
}