#include <iostream>
#include <vector>

using namespace std;

/**
 * Given n non-negative integers representing an elevation map where the
 * width of each bar is 1, compute how much water it is able to trap after
 * raining.
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

int main()
{
    vector<int> arr{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << trap(arr) << endl; // 6
    return 0;
}