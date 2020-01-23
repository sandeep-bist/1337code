#include <iostream>
#include <vector>

using namespace std;

/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start'
 * in the diagram below).
 * The robot can only move either down or right at any point in time. The
 * robot is trying to reach the bottom-right corner of the grid (marked
 * 'Finish' in the diagram below).
 * How many possible unique paths are there?
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

int main()
{
    cout << unique_paths(3, 2) << endl; // 3
    return 0;
}