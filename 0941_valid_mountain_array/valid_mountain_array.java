class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean validMountainArray(int[] arr) {
        int i = 0, j = arr.length;
        if (j < 3) {
            return false;
        }
        while (i + 1 < j && arr[i] < arr[i + 1]) {
            i++;
        }
        if (i == 0 || i == j - 1) {
            return false;
        }
        while (i + 1 < j && arr[i] > arr[i + 1]) {
            i++;
        }
        return (i == j - 1);
    }
}