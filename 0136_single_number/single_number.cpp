#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int single_number(vector<int> &nums)
{
    int res = 0;
    for (auto i : nums)
        res ^= i;
    return res;
}