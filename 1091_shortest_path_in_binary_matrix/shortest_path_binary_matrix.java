class Solution {
    // Time: O(n**2)
    // Space: O(n)
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }
        int dirs[][] = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, -1}, {-1, 1}, {-1, -1}, {1, 1}};
        boolean[][] seen = new boolean[n][n];
        seen[0][0] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] pop = queue.remove();
                if(pop[0] == n - 1 && pop[1] == n - 1) {
                    return pop[2];
                }
                for (int[] dir: dirs) {
                    int x = dir[0] + pop[0];
                    int y = dir[1] + pop[1];
                    if (x >=0 && x < n && y >= 0 && y < n && !seen[x][y] && grid[x][y]==0) {
                        queue.add(new int[]{x, y, pop[2] + 1});
                        seen[x][y]=true;
                    }
                }
            }
        }
        return -1;
    }
}