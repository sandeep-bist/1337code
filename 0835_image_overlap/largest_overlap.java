import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    // Time: O(n**4)
    // Space: O(n**2)
    public int largestOverlap(int[][] A, int[][] B) {
        int rows = A.length, cols = A[0].length;
        List<int[]> a = new ArrayList<>(), b = new ArrayList<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (A[r][c] == 1) {
                    a.add(new int[] { r, c });
                }
                if (B[r][c] == 1) {
                    b.add(new int[] { r, c });
                }
            }
        }
        Map<String, Integer> map = new HashMap<>();
        for (int[] pa : a) {
            for (int[] pb : b) {
                String s = (pa[0] - pb[0]) + " " + (pa[1] - pb[1]);
                map.put(s, map.getOrDefault(s, 0) + 1);
            }
        }
        int res = 0;
        for (int count : map.values())
            res = Math.max(res, count);
        return res;
    }
}