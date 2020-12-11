#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int remove_duplicates(vector<int> &nums)
{
    int i = 0;
    for (auto e : nums)
        if (i < 2 || nums[i - 2] < e)
            nums[i++] = e;
    return i;
}