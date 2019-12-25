#include <iostream>
#include <vector>

using namespace std;

/**
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint
 * stopping you from robbing each of them is that adjacent houses have
 * security system connected and it will automatically contact the police
 * if two adjacent houses were broken into on the same night.
 * Given a list of non-negative integers representing the amount of money
 * of each house, determine the maximum amount of money you can rob tonight
 * without alerting the police. 
 */
int rob(vector<int> &nums)
{
    int prev_max = 0, curr_max = 0;
    for (auto i : nums)
    {
        int tmp = max(i + prev_max, curr_max);
        prev_max = curr_max;
        curr_max = tmp;
    }
    return curr_max;
}

int main()
{
    vector<int> arr{1, 2, 3, 1}; // 4
    cout << rob(arr) << endl;

    vector<int> arr2{2, 7, 9, 3, 1}; // 12
    cout << rob(arr2) << endl;
}