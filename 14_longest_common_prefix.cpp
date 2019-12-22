#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 * Write a function to find the longest common prefix string amongst an array
 * of strings. If there is no common prefix, return an empty string "".
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

int main()
{
    vector<string> strings{"flower", "flow", "flight"};
    cout << longest_common_prefix(strings) << endl; // fl

    vector<string> strings2{"aa", "aa"};
    cout << longest_common_prefix(strings2) << endl; // aa

    return 0;
}