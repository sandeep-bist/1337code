#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
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
