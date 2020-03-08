#include <iostream>
#include <queue>
#include <vector>

using namespace std;

/**
 * Time: O(n * log(n))
 * Space: O(n)
 */
int connectSticks(vector<int> &sticks)
{
    // Syntax to create a min heap for priority queue
    // priority_queue <int, vector<int>, greater<int>> g = gq;
    priority_queue<int, vector<int>, greater<int>> qu(sticks.begin(), sticks.end());
    int result = 0;
    while (qu.size() > 1)
    {
        int a = qu.top();
        qu.pop();
        int b = qu.top();
        qu.pop();
        result += a + b;
        qu.push(a + b);
    }
    return result;
}