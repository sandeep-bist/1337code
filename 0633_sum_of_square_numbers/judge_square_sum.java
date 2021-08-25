class Solution {
    // Time: O(log(n))
    // Space: O(1)
    public boolean judgeSquareSum(int c) {
        if (c < 0) {
            return false;
        }
        int start = 0, end = (int)Math.sqrt(c);
        while (start <= end) {
            int curr = start * start + end * end;
            if (curr == c) {
                return true;
            }
            if (curr < c) {
                start++;
            } else {
                end--;
            }
        }
        return false;
    }
}