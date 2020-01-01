#include <iostream>
#include <vector>

using namespace std;

/**
 * Partitions an array with last element as pivot.
 */
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

/**
 * Quick-select algorithm.
 */
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
 * Find the kth largest element in an unsorted array. Note that it is the kth
 * largest element in the sorted order, not the kth distinct element. 
 */
int find_kth_largest(vector<int> &nums, int k)
{
    int size = nums.size();
    return select(nums, 0, size - 1, size - k);
}

int main()
{
    vector<int> arr{3, 2, 1, 5, 6, 4};
    cout << find_kth_largest(arr, 2) << endl;
    return 0;
}