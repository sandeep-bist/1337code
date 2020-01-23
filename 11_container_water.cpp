#include <iostream>
#include <climits>
#include <vector>

using namespace std;

/**
 * Given n non-negative integers a1, a2, ..., an , where each represents a
 * point at coordinate (i, ai). n vertical lines are drawn such that the
 * two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
 * together with x-axis forms a container, such that the container contains
 * the most water.
 * You may not slant the container and n is at least 2. 
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

int main()
{
    vector<int> arr{1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << max_area(arr) << endl; // 49

    return 0;
}