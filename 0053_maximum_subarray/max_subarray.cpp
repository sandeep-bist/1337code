#include <algorithm> // *max_element()
#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int max_subarray(vector<int> &nums)
{
    if (!nums.size())
        return 0;
    int max_so_far = nums[0];
    int max_curr = nums[0];
    for (int i = 1; i < nums.size(); i++)
    {
        max_curr = max(nums[i], nums[i] + max_curr);
        max_so_far = max(max_so_far, max_curr);
    }
    return max_so_far;
}

/**
 * Time: O(n)
 * Space: O(1)
 */
int max_subarray_kadane(vector<int> &nums)
{
    if (!nums.size())
        return 0;
    for (int i = 1; i < nums.size(); i++)
        if (nums[i - 1] > 0)
            nums[i] = nums[i] + nums[i - 1];
    return *max_element(nums.begin(), nums.end());
}