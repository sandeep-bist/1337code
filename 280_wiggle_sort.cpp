#include <iostream>
#include <vector>

using namespace std;

/**
 * Given an unsorted array nums, reorder it in-place such that
 * nums[0] <= nums[1] >= nums[2] <= nums[3]....
 */
void wiggle_sort(vector<int> &nums)
{
    if (!nums.size())
        return;
    for (int i = 0; i < nums.size() - 1; i++)
        if ((i % 2 == 0) == nums[i] > nums[i + 1])
            swap(nums[i], nums[i + 1]);
}

int main()
{
    vector<int> arr{3, 5, 2, 1, 6, 4};
    wiggle_sort(arr);
    for (auto i : arr)
        cout << i << " "; // 3 5 1 6 2 4
    return 0;
}