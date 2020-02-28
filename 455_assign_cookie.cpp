#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Assume you are an awesome parent and want to give your children some
 * cookies. But, you should give each child at most one cookie. Each
 * child i has a greed factor gi, which is the minimum size of a cookie
 * that the child will be content with; and each cookie j has a size sj.
 * If sj >= gi, we can assign the cookie j to the child i, and the child
 * i will be content. Your goal is to maximize the number of your content
 * children and output the maximum number.
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