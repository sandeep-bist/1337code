#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int missing_number(vector<int> &nums)
{
    int missing = nums.size() * (nums.size() + 1) / 2;
    return missing - accumulate(nums.begin(), nums.end(), 0);
}
