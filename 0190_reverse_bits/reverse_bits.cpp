#include <iostream>

using namespace std;

uint32_t reverseBits(uint32_t n)
{
    uint32_t res = 0;
    for (uint32_t i = 31; n; i--, n >>= 1)
        res += (n & 1) << i;
    return res;
}
