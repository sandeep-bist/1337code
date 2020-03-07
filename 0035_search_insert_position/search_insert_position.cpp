#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(log(n))
 * Space: O(1)
 */
int search_insert(vector<int> &nums, int target)
{
    int start = 0;
    int end = nums.size() - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (nums[mid] > target)
            end = mid - 1;
        else if (nums[mid] < target)
            start = mid + 1;
        else
            return mid;
    }
    return start;
}