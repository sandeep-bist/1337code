#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

/**
 * Depth-first search.
 */
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
 * Given a set of candidate numbers (candidates) (without duplicates) and a
 * target number (target), find all unique combinations in candidates where
 * the candidate numbers sums to target.
 * The same repeated number may be chosen from candidates unlimited number
 * of times.
 */
vector<vector<int>> combination_sum(vector<int> &candidates, int target)
{
    vector<vector<int>> res;
    vector<int> sub;
    sort(candidates.begin(), candidates.end());
    dfs(candidates, sub, 0, target, res);
    return res;
}

int main()
{
    vector<int> arr{2, 3, 6, 7};
    vector<vector<int>> res = combination_sum(arr, 7);
    for (auto s : res)
    {
        for (auto i : s)
            cout << i << " ";
        cout << endl;
    }
    // 2 2 3
    // 7
    return 0;
}