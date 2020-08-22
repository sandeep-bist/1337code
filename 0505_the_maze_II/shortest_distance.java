public class Solution {
    // Time: O(n * m * log(n * m))
    // Space: O(n * m)
    public int shortestDistance(int[][] maze, int[] start, int[] dest) {
        int[][] distance = new int[maze.length][maze[0].length];
        for (int[] row : distance)
            Arrays.fill(row, Integer.MAX_VALUE);
        distance[start[0]][start[1]] = 0;
        dijkstra(maze, start, distance);
        int finalDest = distance[dest[0]][dest[1]];
        return finalDest == Integer.MAX_VALUE ? -1 : finalDest;
    }

    public void dijkstra(int[][] maze, int[] start, int[][] distance) {
        int[][] dirs = { { 0, 1 }, { 0, -1 }, { -1, 0 }, { 1, 0 } };
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        queue.offer(new int[] { start[0], start[1], 0 });
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            if (distance[curr[0]][curr[1]] < curr[2])
                continue;
            for (int[] dir : dirs) {
                int x = dir[0], y = dir[1], count = 0;
                int r = curr[0], c = curr[1];
                while (r + x >= 0 && c + y >= 0 && r + x < maze.length && c + y < maze[0].length
                        && maze[r + x][c + y] == 0) {
                    r += x;
                    c += y;
                    count++;
                }
                int curr_dist = distance[curr[0]][curr[1]] + count;
                if (curr_dist < distance[r][c]) {
                    distance[r][c] = curr_dist;
                    queue.offer(new int[] { r, c, curr_dist });
                }
            }
        }
    }
}