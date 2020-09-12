import java.util.List;
import java.util.ArrayList;

class Solution {
    // Time: O((9! * k)/9 - k)
    // Space: O(k)
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        backTrack(res, new ArrayList<Integer>(), k, n, 1);
        return res;
    }

    private void backTrack(List<List<Integer>> res, ArrayList<Integer> curr, int k, int n, int start) {
        if (curr.size() > k) {
            return;
        }
        if (curr.size() == k && n == 0) {
            res.add(new ArrayList<Integer>(curr));
            return;
        }
        for (int i = start; i <= 9; i++) {
            if (n - i >= 0) {
                curr.add(i);
                backTrack(res, curr, k, n - i, i + 1);
                curr.remove(curr.size() - 1);
            }
        }
    }
}