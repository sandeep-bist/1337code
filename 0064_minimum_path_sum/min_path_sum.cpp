#include <iostream>
#include <climits>
#include <vector>

using namespace std;

/**
 * Time: O(m * n)
 * Space: O(1)
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
