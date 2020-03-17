#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n) 
 * Space: O(1)
 */
void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int i = m - 1, j = n - 1, end = m + n - 1;
    while (j >= 0)
        nums1[end--] = (i < 0 || nums1[i] < nums2[j]) ? nums2[j--] : nums1[i--];
}
