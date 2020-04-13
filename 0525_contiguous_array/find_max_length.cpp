#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(n)
 */
int find_max_length(vector<int> &nums)
{
    unordered_map<int, int> indexes;
    indexes[0] = -1;
    int res = 0, tmp = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        tmp += nums[i] ? 1 : -1;
        if (indexes.count(tmp))
            res = max(res, i - indexes[tmp]);
        else
            indexes[tmp] = i;
    }
    return res;
}
