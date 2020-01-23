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
 * A 2d grid map of m rows and n columns is initially filled with water.
 * We may perform an addLand operation which turns the water at position
 * (row, col) into a land. Given a list of positions to operate, count the
 * number of islands after each addLand operation. An island is surrounded
 * by water and is formed by connecting adjacent lands horizontally or
 * vertically. You may assume all four edges of the grid are all surrounded
 * by water.
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

int main()
{
    vector<vector<int>> arr{{0, 0},
                            {0, 1},
                            {1, 2},
                            {2, 1}};
    vector<int> res = num_islands2(3, 3, arr);
    for (auto i : res)
        cout << i << " "; // 1, 1, 2, 3
    cout << endl;

    vector<vector<int>> arr2{{0, 0},
                             {0, 1},
                             {1, 2},
                             {1, 2}};
    vector<int> res2 = num_islands2(3, 3, arr2);
    for (auto i : res2)
        cout << i << " "; // 1, 1, 2, 2
    return 0;
}