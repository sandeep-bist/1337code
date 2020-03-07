#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
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