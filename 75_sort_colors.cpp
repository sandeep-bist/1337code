#include <iostream>
#include <vector>

using namespace std;

/**
 * Given an array with n objects colored red, white or blue, sort them
 * in-place so that objects of the same color are adjacent, with the
 * colors in the order red, white and blue.
 * 
 * Here, we will use the integers 0, 1, and 2 to represent the color red,
 * white, and blue respectively.
 * Do not return anything, modify nums in-place instead. 
 */
void sortColors(vector<int> &nums)
{
    int c = 0, p0 = 0, p2 = nums.size() - 1;
    while (c <= p2)
    {
        if (nums[c] == 0)
            swap(nums[c++], nums[p0++]);
        else if (nums[c] == 2)
            swap(nums[c], nums[p2--]);
        else
            c++;
    }
}

int main()
{
    vector<int> arr{2, 0, 2, 1, 1, 0};
    sortColors(arr);
    for (auto i : arr)
        cout << i << " ";
    /* 0 0 1 1 2 2 */
    return 0;
}