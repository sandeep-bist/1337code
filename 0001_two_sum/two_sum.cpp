#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

/**
 * Time: O(n)
 * Space: O(n)
 */
vector<int> two_sum(vector<int> &nums, int target)
{
    vector<int> res;
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++)
    {
        int compliment = target - nums[i];
        if (map.count(compliment))
        {
            res.push_back(i);
            res.push_back(map[compliment]);
            return res;
        }
        map[nums[i]] = i;
    }
    return res;
}