#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(m * n)
 * Space: O(m * n)
 */
int unique_paths(int m, int n)
{
    vector<vector<int>> dp;
    // Inititalizing nested vector with all 1's.
    for (int i = 0; i < m; i++)
    {
        vector<int> sub(n, 1);
        dp.push_back(sub);
    }
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    return dp[m - 1][n - 1];
}