public class Solution {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int remainder = x % 10;
            int tmp = res * 10 + remainder;
            // if overflow happens, then next statement will be true
            if ((tmp - remainder) / 10 != res) {
                return 0;
            }
            res = tmp;
            x /= 10;
        }
        return res;
    }
}
