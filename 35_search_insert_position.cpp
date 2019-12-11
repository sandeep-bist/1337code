#include <iostream>
#include <vector>

using namespace std;

/**
 * Given a sorted array and a target value, return the index if the target
 * is found. If not, return the index where it would be if it were inserted
 * in order.
 * You may assume no duplicates in the array.
 */
int searchInsert(vector<int> &nums, int target)
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

int main()
{
    vector<int> arr{1, 3, 5, 6};
    cout << searchInsert(arr, 5) << endl; // 2
    cout << searchInsert(arr, 7) << endl; // 4
    cout << searchInsert(arr, 0) << endl; // 0
    return 0;
}