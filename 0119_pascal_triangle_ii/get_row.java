// Time: O(n**2)
// Space: O(n)
class Solution {
    public static List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        res.add(1);
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i - 1; j >= 1; j--) {
                int tmp = res.get(j - 1) + res.get(j);
                res.set(j, tmp);
            }
            res.add(1);
        }
        return res;
    }
}