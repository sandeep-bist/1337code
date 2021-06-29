#include <iostream>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
bool is_palindrome(int x)
{
    if (x < 0 || isFactorOfTen(x)) {
        return false;
    }
    int reverse = 0;
    while (x > reverse)
    {
        reverse = (reverse * 10) + x % 10;
        x /= 10;
    }
    return x == reverse || x == (reverse / 10);
}

bool isFactorOfTen(int x) {
    return x && x % 10 == 0;
}