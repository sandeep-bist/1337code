#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

/**
 * Time: O(n)
 * Space: O(n)
 */ 
bool contains_duplicate(vector<int> &nums)
{
    unordered_set<int> set;
    for (auto i : nums)
        set.insert(i);
    return set.size() != nums.size();
}
