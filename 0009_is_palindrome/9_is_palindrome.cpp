#include <iostream>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
bool isPalindrome(int x)
{
    if (x < 0 || (x && x % 10 == 0))
        return false;
    int rev = 0;
    while (x > rev)
    {
        rev = (rev * 10) + x % 10;
        x /= 10;
    }
    return x == rev || x == (rev / 10);
}