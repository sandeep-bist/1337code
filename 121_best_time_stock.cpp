#include <climits>
#include <iostream>
#include <vector>

using namespace std;

/**
 * Say you have an array for which the ith element is the price of a given
 * stock on day i. If you were only permitted to complete at most one
 * transaction (i.e., buy one and sell one share of the stock), design an
 * algorithm to find the maximum profit.
 * Note that you cannot sell a stock before you buy one.
 */
int max_profit(vector<int> &prices)
{
    int min_price = INT_MAX;
    int max_profit = 0;
    for (auto i : prices)
    {
        if (i < min_price)
            min_price = i;
        else if (i - min_price > max_profit)
            max_profit = i - min_price;
    }
    return max_profit;
}

int main()
{
    vector<int> arr{7, 1, 5, 3, 6, 4}; // 5
    cout << max_profit(arr) << endl;

    vector<int> arr2{7, 5, 4, 3, 2, 1}; // 0
    cout << max_profit(arr2) << endl;

    vector<int> arr3{2, 4, 1, 2}; // 2
    cout << max_profit(arr3) << endl;

    return 0;
}