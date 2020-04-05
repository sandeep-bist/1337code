#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int max_profit(vector<int> &prices)
{
    int profits = 0;
    for (int i = 1; i < prices.size(); i++)
        if (prices[i] > prices[i - 1])
            profits += prices[i] - prices[i - 1];
    return profits;
}
