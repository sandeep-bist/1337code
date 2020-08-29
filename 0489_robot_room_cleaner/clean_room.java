/**
 * This is the robot's control interface. // You should not implement it, or
 * speculate about its implementation interface Robot { // Returns true if the
 * cell in front is open and robot moves into the cell. // Returns false if the
 * cell in front is blocked and robot stays in the current cell. public boolean
 * move();
 *
 * Robot will stay in the same cell after calling turnLeft/turnRight. // Each
 * turn will be 90 degrees. public void turnLeft(); public void turnRight();
 *
 * Clean the current cell. public void clean(); }
 */

class Solution {
    Set<Pair<Integer, Integer>> visited = new HashSet();
    Robot robot;

    private void goBack() {
        robot.turnLeft();
        robot.turnLeft();
        robot.move();
        robot.turnLeft();
        robot.turnLeft();
    }

    public void backtrack(int row, int col, int rx, int ry) {
        visited.add(new Pair(row, col));
        robot.clean();
        for (int i = 0; i < 4; ++i) {
            if (!visited.contains(new Pair(row + rx, col + ry)) && robot.move()) {
                backtrack(row + rx, col + ry, rx, ry);
            }
            robot.turnLeft();
            int tmp = rx;
            rx = -ry;
            ry = tmp;
        }
        goBack();
    }

    public void cleanRoom(Robot robot) {
        this.robot = robot;
        backtrack(0, 0, 0, 1);
    }
}