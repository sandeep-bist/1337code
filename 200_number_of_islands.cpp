#include <iostream>
#include <vector>

using namespace std;

/**
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges
 * of the grid are all surrounded by water.
 */
int num_islands(vector<vector<char>> &grid)
{
    int islands = 0;
    for (int i = 0; i < grid.size(); i++)
        for (int j = 0; j < grid[0].size(); j++)
            if (grid[i][j] == '1')
                islands += dfs(grid, i, j);
    return islands;
}

/**
 * Depth-first search.
 */
int dfs(vector<vector<char>> &grid, int row, int col)
{
    if (row < 0 || col < 0 || row >= grid.size() ||
        col >= grid[0].size() || grid[row][col] == '0')
        return 0;
    grid[row][col] = '0';
    dfs(grid, row - 1, col);
    dfs(grid, row, col - 1);
    dfs(grid, row + 1, col);
    dfs(grid, row, col + 1);
    return 1;
}

/*
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3
*/