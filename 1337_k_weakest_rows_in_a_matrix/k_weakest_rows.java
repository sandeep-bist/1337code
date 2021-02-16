class Solution {
    // Time: O(log(n) * m)
    // Space: O(n * m)
    public int[] kWeakestRows(int[][] mat, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0] ? b[0] - a[0] : b[1] - a[1]);
        int[] res = new int[k];
        for (int i = 0; i < mat.length; i++) {
            int ones = countOnes(mat[i]);
            pq.offer(new int[]{ones, i});
            if (pq.size() > k) {
                pq.poll();
            }
        }
        while (k > 0) {
            res[--k] = pq.poll()[1];
        }
        return res;
    }
    
    private int countOnes(int[] arr) {
        int i = 0, j = arr.length;
        while (i < j) {
            int mid = (i + j) / 2;
            if (arr[mid] == 1) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        return i;
    }
}