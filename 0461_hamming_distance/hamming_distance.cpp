#include <iostream>

using namespace std;

// Time: O(1)
// Space: O(1)
int hamming_distance(int x, int y)
{
    int xy, res;
    for (xy = x ^ y, res = 0; xy; res++)
        xy &= xy - 1;
    return res;
}
