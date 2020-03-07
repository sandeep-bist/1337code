#include <iostream>
#include <climits>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int max_area(vector<int> &height)
{
    int l = 0;
    int r = height.size() - 1;
    int maximum = INT_MIN;
    while (l < r)
    {
        int minimum = min(height[l], height[r]);
        maximum = max(maximum, minimum * (r - l));
        height[r] > height[l] ? l++ : r--;
    }
    return maximum;
}
