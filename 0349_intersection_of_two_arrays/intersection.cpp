#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

/**
 * Time: O(m + n)
 * Space: O(m + n)
 */
vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    unordered_set<int> s{nums1.begin(), nums1.end()};
    vector<int> res;
    for (auto i : nums2)
        if (s.erase(i))
            res.push_back(i);
    return res;
}