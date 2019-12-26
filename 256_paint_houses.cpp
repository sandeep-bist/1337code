#include <iostream>
#include <vector>

using namespace std;

/**
 * There are a row of n houses, each house can be painted with one of the
 * three colors: red, blue or green. The cost of painting each house with
 * a certain color is different. You have to paint all the houses such that
 * no two adjacent houses have the same color.
 * The cost of painting each house with a certain color is represented by a
 * n x 3 cost matrix. For example, costs[0][0] is the cost of painting house
 * 0 with color red; costs[1][2] is the cost of painting house 1 with color
 * green, and so on... Find the minimum cost to paint all houses.
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

int main()
{
    vector<vector<int>> arr{{17, 2, 17}, {16, 16, 5}, {14, 3, 19}};
    cout << min_cost(arr) << endl; // 10
    return 0;
}