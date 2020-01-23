#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int>> three_sum(vector<int> &nums)
{
    vector<vector<int>> res;
    if (!nums.size())
        return res;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (i > 0 && nums[i] == nums[i - 1])
            continue;
        int j = i + 1;
        int k = nums.size() - 1;
        while (j < k)
        {
            int sum = nums[i] + nums[j] + nums[k];
            if (sum < 0)
                j++;
            else if (sum > 0)
                k--;
            else
            {
                res.push_back({nums[i], nums[j], nums[k]});
                while (j < k && nums[j] == nums[j + 1])
                    j++;
                while (j < k && nums[k] == nums[k - 1])
                    k--;
                j++;
                k--;
            }
        }
    }
    return res;
}

int main()
{
    vector<int> arr{-1, 0, 1, 2, -1, -4};
    vector<vector<int>> res = three_sum(arr);
    for (auto sub : res)
    {
        for (auto i : sub)
            cout << i << " ";
        cout << endl;
    }
    /* 
    -1 -1 2
    -1 0 1
    */
}