#include <iostream>
#include <unordered_set>
#include <vector>


/**
 * Time: O(n) 
 * Space: O(n)
 */
int count_elements(vector<int> &arr)
{
    unordered_set<int> s{arr.begin(), arr.end()};
    int count = 0;
    for (auto i : arr)
        if (s.count(i + 1))
            count++;
    return count;
}