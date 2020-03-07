#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int min_cost(vector<vector<int>> &costs)
{
    if (!costs.size())
        return 0;
    int s = costs.size();
    for (int i = 1; i < s; i++)
    {
        vector<int> prev = costs[i - 1];
        costs[i][0] += min(prev[1], prev[2]);
        costs[i][1] += min(prev[0], prev[2]);
        costs[i][2] += min(prev[0], prev[1]);
    }
    vector<int> last = costs[s - 1];
    return min(min(last[0], last[1]), last[2]);
}
