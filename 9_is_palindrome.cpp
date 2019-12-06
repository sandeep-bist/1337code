#include <iostream>

using namespace std;

/**
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 * Could you solve it without converting the integer to a string?
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

int main()
{
    cout << isPalindrome(123321) << endl;  // 1
    cout << isPalindrome(1234321) << endl; // 1
    cout << isPalindrome(123421) << endl;  // 0

    return 0;
}