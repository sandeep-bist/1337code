#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int trap(vector<int> &height)
{
    int res = 0, l = 0, l_max = 0, r_max = 0, r = height.size() - 1;
    if (!height.size())
        return res;
    while (l < r)
    {
        if (height[r] > height[l])
        {
            height[l] > l_max
                ? l_max = height[l]
                : res += l_max - height[l];
            l++;
        }
        else
        {
            height[r] > r_max
                ? r_max = height[r]
                : res += r_max - height[r];
            r--;
        }
    }
    return res;
}