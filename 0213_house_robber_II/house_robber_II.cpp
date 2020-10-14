#include <iostream>
#include <vector>

using namespace std;

int rob(vector<int> &nums)
{
    int prev = 0, curr = 0;
    for (auto i : nums)
    {
        int temp = max(curr, prev + i);
        prev = curr;
        curr = temp;
    }
    return curr;
}

// Time: O(n)
// Space: O(1)
int rob_again(vector<int> &nums)
{
    vector<int> exclude_first, exclude_last;
    // Slicing arrays, could be better way to do this.
    for (int i = 0; i < nums.size() - 1; i++)
        exclude_last.push_back(nums[i]);
    for (int i = 1; i < nums.size(); i++)
        exclude_first.push_back(nums[i]);
    return max(rob(exclude_first), rob(exclude_last));
}