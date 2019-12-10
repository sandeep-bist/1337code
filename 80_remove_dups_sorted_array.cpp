#include <iostream>
#include <vector>

using namespace std;

/**
 * Given a sorted array nums, remove the duplicates in-place such that 
 * duplicates appeared at most twice and return the new length.
 * Do not allocate extra space for another array, you must do this by
 * modifying the input array in-place with O(1) extra memory. 
 */
int removeDuplicates(vector<int> &nums)
{
    int i = 0;
    for (auto e : nums)
        if (i < 2 || nums[i - 2] < e)
            nums[i++] = e;
    return i;
}

int main()
{
    vector<int> arr{1, 1, 1, 2, 2, 3};
    cout << removeDuplicates(arr) << endl; // 5
    return 0;
}