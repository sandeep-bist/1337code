#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
void wiggle_sort(vector<int> &nums)
{
    if (!nums.size())
        return;
    for (int i = 0; i < nums.size() - 1; i++)
        if ((i % 2 == 0) == nums[i] > nums[i + 1])
            swap(nums[i], nums[i + 1]);
}
