#include <algorithm> // *max_element()
#include <iostream>
#include <vector>

using namespace std;

/**
 * Given an integer array nums, find the contiguous subarray (containing
 * at least one number) which has the largest sum and return its sum.
 */
int max_sub_array(vector<int> &nums)
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
 * Alternate solution that modifies array as you iterate. 
 */
int max_sub_array_kadane(vector<int> &nums)
{
    if (!nums.size())
        return 0;
    for (int i = 1; i < nums.size(); i++)
        if (nums[i - 1] > 0)
            nums[i] = nums[i] + nums[i - 1];
    return *max_element(nums.begin(), nums.end());
}

int main()
{
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << max_sub_array(nums) << endl; // 6

    vector<int> nums2{};
    cout << max_sub_array(nums2) << endl; // 0

    return 0;
}