#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Time: O(2 * n * log(n) + n)
 * Space: O(1)
 */
int find_content_children(vector<int> &g, vector<int> &s)
{
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int kid = 0, cookie = 0;
    while (kid < g.size() && cookie < s.size())
    {
        if (s[cookie] >= g[kid])
            kid++;
        cookie++;
    }
    return kid;
}