#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n) 
 * Space: O(n)
 */
vector<vector<int>> flood_fill(vector<vector<int>> &image, int sr,
                               int sc, int new_color)
{
    int old_color = image[sr][sc];
    if (old_color == new_color)
        return image;
    fill(image, sr, sc, old_color, new_color);
    return image;
}

void fill(vector<vector<int>> &image, int r, int c,
          int old_color, int new_color)
{
    if (r < 0 || c < 0 || r >= image.size() || c >= image[0].size())
        return;
    if (image[r][c] == old_color)
    {
        image[r][c] = new_color;
        fill(image, r + 1, c, old_color, new_color);
        fill(image, r - 1, c, old_color, new_color);
        fill(image, r, c + 1, old_color, new_color);
        fill(image, r, c - 1, old_color, new_color);
    }
}
