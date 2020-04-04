#include <iostream>
#include <vector>

/**
 * Time: O(n)
 * Space: O(1)
 */
void moveZeroes(vector<int> &nums)
{
    int i = 0, j = 0;
    for (; j < nums.size(); j++)
    {
        if (nums[j])
        {
            if (i != j)
                nums[i] = nums[j];
            i++;
        }
    }
    for (; i < nums.size(); i++)
        nums[i] = 0;
}
