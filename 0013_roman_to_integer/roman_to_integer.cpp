#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1)
 */
int roman_to_int(string s)
{
    unordered_map<char, int> map = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}};
    int sum = 0, prev = 0;
    for (int i = s.length() - 1; i >= 0; i--)
    {
        int curr = map[s[i]];
        sum += curr < prev ? -curr : curr;
        prev = curr;
    }
    return sum;
}
