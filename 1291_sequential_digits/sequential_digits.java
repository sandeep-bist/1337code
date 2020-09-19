import java.util.List
import java.util.ArrayList;

class Solution {
    // Time: O(1)
    // Space: O(1)
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> res = new ArrayList<>();
        String nums = "123456789";
        int minDigits = String.valueOf(low).length(), maxDigits = String.valueOf(high).length();
        for (int i = minDigits; i < maxDigits + 1; i++) {
            for (int j = 0; j < 10 - i; j++) {
                int tmp = Integer.parseInt(nums.substring(j, j + i));
                if (tmp >= low && tmp <= high) {
                    res.add(tmp);
                }
            }

        }
        return res;
    }
}
