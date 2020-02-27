#include <iostream>

using namespace std;

/**
 * Balanced strings are those who have equal quantity of 'L' and 'R'
 * characters.
 * Given a balanced string s split it in the maximum amount of balanced
 * strings.
 * Return the maximum amount of splitted balanced strings.
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
