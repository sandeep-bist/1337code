#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(n) 
 */
int get_sum(int a, int b)
{
    return b == 0 ? a : getSum(a ^ b, (unsigned int)(a & b) << 1);
}