#include <iostream>
#include <string>
#include <unordered_map>

/**
 * Given a roman numeral, convert it to an integer. Input is guaranteed to be
 * within the range from 1 to 3999.
 */
int romanToInt(string s)
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

int main()
{
    cout << romanToInt("MCMXCIV") << endl; // 1994
    cout << romanToInt("IX") << endl;      // 9
    return 0;
}