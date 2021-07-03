class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int i = n - 1;
        while (i >= 0 && digits[i] == 9) {
            digits[i] = 0;
            i--;
        }
        if (i < 0) {
            int res[] = new int[n + 1];
            res[0] = 1;
            return res;
        }
        digits[i]++;
        return digits;
    }
}