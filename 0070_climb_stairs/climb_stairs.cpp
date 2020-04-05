#include <iostream>
#include <vector>

/**
 * Time: O(n)
 * Space: O(n) 
 */
int climb_stairs(int n)
{
    if (n == 1)
        return 1;
    vector<int> res(n, 0);
    res[0] = 1;
    res[1] = 2;
    for (int i = 2; i < n; i++)
        res[i] = res[i - 2] + res[i - 1];
    return res[n - 1];
}