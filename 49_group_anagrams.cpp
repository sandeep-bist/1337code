#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

/**
 * Given an array of strings, group anagrams together.
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

int main()
{
    vector<string> arr{"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> res = group_anagrams(arr);
    for (auto sub : res)
    {
        for (auto s : sub)
            cout << s << " ";
        cout << endl;
    }
    /*
    bat
    eat tea ate
    tan nat
    */
}