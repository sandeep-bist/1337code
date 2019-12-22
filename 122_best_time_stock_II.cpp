#include <iostream>
#include <vector>

using namespace std;

/**
 * Say you have an array for which the ith element is the price of a given
 * stock on day i.
 * Design an algorithm to find the maximum profit. You may complete as many
 * transactions as you like (i.e., buy one and sell one share of the stock
 * multiple times).
 * Note: You may not engage in multiple transactions at the same time (i.e.,
 * you must sell the stock before you buy again).
 */
int max_profit(vector<int> &prices)
{
    int profits = 0;
    for (int i = 1; i < prices.size(); i++)
        if (prices[i] > prices[i - 1])
            profits += prices[i] - prices[i - 1];
    return profits;
}

int main()
{
    vector<int> arr{7, 1, 5, 3, 6, 4}; // 7
    cout << max_profit(arr) << endl;

    vector<int> arr2{7, 5, 4, 3, 2, 1}; // 0
    cout << max_profit(arr2) << endl;

    vector<int> arr3{1, 2, 3, 4, 5}; // 4
    cout << max_profit(arr3) << endl;
    return 0;
}