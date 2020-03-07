#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void dfs(vector<int> &nums, vector<int> &sub, int index, int target,
         vector<vector<int>> &res)
{
    if (target == 0)
    {
        res.push_back(sub);
        return;
    }
    for (int i = index; i < nums.size(); i++)
    {
        if (nums[i] > target)
            break;
        sub.push_back(nums[i]);
        dfs(nums, sub, i, target - nums[i], res);
        sub.pop_back();
    }
}

/**
 * Time: O(n * log(n) + 2**n)
 * Space: O(n**2)
 */
vector<vector<int>> combination_sum(vector<int> &candidates, int target)
{
    vector<vector<int>> res;
    vector<int> sub;
    sort(candidates.begin(), candidates.end());
    dfs(candidates, sub, 0, target, res);
    return res;
}