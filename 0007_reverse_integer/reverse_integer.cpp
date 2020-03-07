#include <iostream>
#include <climits>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int reverse(int x)
{
    long res = 0;
    while (x)
    {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return res < INT_MAX && res > INT_MIN ? res : 0;
}