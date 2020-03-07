#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 * Time: O(m * n)
 * Space: O(1)
 */
string longestCommonPrefix(vector<string> &strs)
{
    if (!strs.size())
        return "";
    string first = strs[0];
    for (int i = 0; i < first.size(); i++)
    {
        char c = first[i];
        for (auto str : strs)
            if (!str.size() || str[i] != c)
                return first.substr(0, i);
    }
    return first;
}