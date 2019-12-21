#include <iostream>
#include <climits>

using namespace std;

/**
 * Given a 32-bit signed integer, reverse digits of an integer.
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

int main()
{
    cout << reverse(123) << endl;  // 321
    cout << reverse(120) << endl;  // 21
    cout << reverse(-914) << endl; // -419
    return 0;
}