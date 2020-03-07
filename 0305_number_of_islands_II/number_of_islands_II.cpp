#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class DSU
{
public:
    unordered_map<int, int> parents;
    int count = 0;
    int find(int x);
    void union_(int x, int y);
    void add(int x);
};

/**
 Finds parent of element with path compression functionality.
 */
int DSU::find(int x)
{
    if (this->parents[x] != x)
        this->parents[x] = this->find(this->parents[x]);
    return this->parents[x];
}

/**
 * Combines parent of two elements if they do not match.
 */
void DSU::union_(int x, int y)
{
    int par_x = this->find(x);
    int par_y = this->find(y);
    if (par_x != par_y)
    {
        this->count--;
        this->parents[par_x] = par_y;
    }
}

/**
 * Adds an element into DSU.
 */
void DSU::add(int x)
{
    if (this->parents.count(x))
        return;
    this->parents[x] = x;
    this->count++;
}

/**
 * Time: O(m * n + L) where L is the number of operations
 * Space: O(m * n)
 */
vector<int> num_islands2(int m, int n, vector<vector<int>> positions)
{
    vector<vector<int>> surroundings{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    DSU dsu;
    vector<int> res;
    for (auto p : positions)
    {
        int key = p[0] * n + p[1];
        dsu.add(key);
        for (auto s : surroundings)
        {
            int r = p[0] + s[0];
            int c = p[1] + s[1];
            int tmp = r * n + c;
            if (r >= 0 && r < m && c >= 0 && c < n && dsu.parents.count(tmp))
                dsu.union_(key, tmp);
        }
        res.push_back(dsu.count);
    }
    return res;
}
