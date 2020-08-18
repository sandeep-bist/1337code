// Time: O(n * 2**n)
// Space: O(2**n)
class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        if (n == 1) {
            return new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        }
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 1; i < 10; i++) {
            dfs(n - 1, i, k, res);
        }
        return res.stream().mapToInt(i -> i).toArray();
    }

    private void dfs(int n, int num, int k, List<Integer> res) {
        if (n == 0) {
            res.add(num);
            return;
        }
        int tail = num % 10;
        if (tail + k < 10) {
            dfs(n - 1, num * 10 + tail + k, k, res);
        }
        if (k > 0 && tail - k >= 0) { // avoid dups when k is 0
            dfs(n - 1, num * 10 + tail - k, k, res);
        }
    }
}