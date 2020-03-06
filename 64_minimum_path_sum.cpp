#include <iostream>
#include <vector>

using namespace std;

/**
 * Given a m x n grid filled with non-negative numbers, find a path from
 * top left to bottom right which minimizes the sum of all numbers along
 * its path.
 * You can only move either down or right at any point in time.
 * O(n * m) space. Can optimize for O(1) if one modifies given matrix.
 */
int min_path_sum(vector<vector<int>> &grid)
{
    int r = grid.size();
    if (r == 0)
        return 0;
    int c = grid[0].size();
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (!i && !j)
                continue;
            int left = !j ? INT_MAX : grid[i][j - 1];
            int up = !i ? INT_MAX : grid[i - 1][j];
            grid[i][j] += min(left, up);
        }
    }
    return grid[r - 1][c - 1];
}
