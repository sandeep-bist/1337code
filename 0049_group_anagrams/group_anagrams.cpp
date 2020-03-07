#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

/**
 * Time: O(m * n * n * log(n))
 * Space: O(m * n * n)
 */
vector<vector<string>> group_anagrams(vector<string> &strs)
{
    unordered_map<string, vector<string>> map;
    vector<vector<string>> res;
    for (auto str : strs)
    {
        string copy = str;
        sort(copy.begin(), copy.end());
        map[copy].push_back(str);
    }
    for (auto m : map)
        res.push_back(m.second);
    return res;
}