//,Time: O(n)
// Space: O(1)
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int i = 0, j = A.length - 1;
        while (i < j) {
            if (A[i] % 2 == 1) {
                while (i < j && A[j] % 2 == 1) {
                    j--;
                }
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
            i++;
        }
        return A;
    }
}