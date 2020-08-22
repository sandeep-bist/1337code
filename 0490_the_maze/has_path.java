// Time: O(m * n)
// Space: O(m * n)
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int[][] dirs = { { 0, 1 }, { 0, -1 }, { -1, 0 }, { 1, 0 } };
        Queue<int[]> queue = new LinkedList<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0], y = curr[1];
            if (x == destination[0] && y == destination[1]) {
                return true;
            }
            maze[x][y] = 2;
            for (int[] dir : dirs) {
                int r = x, c = y;
                while (isValidPath(maze, r + dir[0], c + dir[1])) {
                    r += dir[0];
                    c += dir[1];
                }
                if (maze[r][c] == 0) {
                    queue.add(new int[] { r, c });
                }
            }
        }
        return false;
    }

    private boolean isValidPath(int[][] maze, int row, int col) {
        return row >= 0 && col >= 0 && row < maze.length && col < maze[0].length && maze[row][col] != 1;
    }
}