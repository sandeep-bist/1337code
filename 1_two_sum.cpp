#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

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

int main()
{
    vector<int> arr{2, 7, 11, 15};
    for (auto i : two_sum(arr, 9))
        cout << i << " "; // 1 0
}