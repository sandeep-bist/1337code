# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def goBack(self, robot):
        # 3, Back to previous position and direction
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()

    def cleanRoom(self, robot):
        """
        Time: O(4**(n - m)) where n is the number of cells and m
        is the number of obstacles
        Space: O(n - m)
        """
        path = set()

        def dfs(x, y, dx, dy):
            robot.clean()
            path.add((x, y))
            for _ in range(4):
                if (x + dx, y + dy) not in path and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx
            self.goBack(robot)
        dfs(0, 0, 0, 1)
