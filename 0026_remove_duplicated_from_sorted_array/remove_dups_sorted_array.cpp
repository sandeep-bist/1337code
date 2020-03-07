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
    for (int j : nums)
        if (i < 1 || nums[i - 1] < j)
            nums[i++] = j;
    return i;
}