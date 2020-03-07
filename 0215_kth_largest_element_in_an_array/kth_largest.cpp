#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &nums, int l, int r)
{
    int i = l;
    int pivot = nums[r];
    for (int j = l; j < r; j++)
    {
        if (nums[j] < pivot)
        {
            swap(nums[i], nums[j]);
            i++;
        }
    }
    swap(nums[i], nums[r]);
    return i;
}

int select(vector<int> &nums, int l, int r, int k)
{
    if (l == r)
        return nums[l];
    int p = partition(nums, l, r);
    if (p == k)
        return nums[p];
    if (p > k)
        return select(nums, l, p - 1, k);
    return select(nums, p + 1, r, k);
}

/**
 * Time: O(n)
 * Space: O(1)
 */
int find_kth_largest(vector<int> &nums, int k)
{
    int size = nums.size();
    return select(nums, 0, size - 1, size - k);
}
