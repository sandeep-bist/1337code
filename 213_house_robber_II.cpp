#include <iostream>
#include <vector>

using namespace std;

/**
 * Helper.
 */
int rob(vector<int> &nums)
{
    int prev = 0, curr = 0;
    for (auto i : nums)
    {
        int temp = max(curr, prev + i);
        prev = curr;
        curr = temp;
    }
    return curr;
}

/**
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed. All houses at this
 * place are arranged in a circle. That means the first house is the neighbor
 * of the last one. Meanwhile, adjacent houses have security system connected
 * and it will automatically contact the police if two adjacent houses were
 * broken into on the same night.
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight
 * without alerting the police.
 */
int rob_again(vector<int> &nums)
{
    vector<int> exclude_first, exclude_last;
    // Slicing arrays, could be better way to do this.
    for (int i = 0; i < nums.size() - 1; i++)
        exclude_last.push_back(nums[i]);
    for (int i = 1; i < nums.size(); i++)
        exclude_first.push_back(nums[i]);
    return max(rob(exclude_first), rob(exclude_last));
}

int main()
{
    vector<int> arr{1, 2, 3, 1};
    cout << rob_again(arr) << endl; // 4
    vector<int> arr2{1, 2, 3, 1, 5};
    cout << rob_again(arr2) << endl; // 8
    return 0;
}