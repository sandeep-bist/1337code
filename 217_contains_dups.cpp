#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool contains_duplicate(vector<int> &nums)
{
    unordered_set<int> set;
    for (auto i : nums)
        set.insert(i);
    return set.size() != nums.size();
}

int main()
{
    vector<int> arr{1, 2, 3, 1}; // 1
    cout << contains_duplicate(arr) << endl;

    vector<int> arr2{1, 2, 3}; // 0
    cout << contains_duplicate(arr2) << endl;
    return 0;
}