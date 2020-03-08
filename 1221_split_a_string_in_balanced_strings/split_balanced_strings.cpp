#include <iostream>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int balance_string_split(string s)
{
    int counter = 0, res = 0;
    for (auto c : s)
    {
        if (c == 'L')
            counter++;
        if (c == 'R')
            counter--;
        if (!counter)
            res++;
    }
    return res;
}
