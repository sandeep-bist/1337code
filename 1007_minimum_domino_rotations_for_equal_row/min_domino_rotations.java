class Solution {
    private int[] a;
    private int[] b;

    // Time: O(n)
    // Space: O(1)
    public int minDominoRotations(int[] A, int[] B) {
        a = A;
        b = B;
        int ops = check(a[0]);
        if (ops != -1 || a[0] == b[0]) {
            return ops;
        }
        return check(b[0]);
    }

    private int check(int val) {
        int x = 0, y = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != val && b[i] != val) {
                return -1;
            } else if (a[i] != val) {
                x++;
            } else if (b[i] != val) {
                y++;
            }
        }
        return Math.min(x, y);
    }
}