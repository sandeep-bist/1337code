#include <iostream>
#include <vector>

using namespace std;

/**
 * Given a sorted array nums, remove the duplicates in-place such that each
 * element appear only once and return the new length.
 * Do not allocate extra space for another array, you must do this by
 * modifying the input array in-place with O(1) extra memory.
 */
int removeDuplicates(vector<int> &nums)
{
    int i = 0;
    for (int j : nums)
        if (i < 1 || nums[i - 1] < j)
            nums[i++] = j;
    return i;
}

int main()
{
    vector<int> arr{1, 1, 2};
    cout << removeDuplicates(arr) << endl; // 2
    return 0;
}