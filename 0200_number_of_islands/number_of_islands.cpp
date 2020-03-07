#include <iostream>
#include <vector>

using namespace std;

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

/**
 * Time: O(m * n)
 * Space: O(m * n)
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
