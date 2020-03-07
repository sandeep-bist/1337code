#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool dfs(vector<vector<char>> matrix, int r, int c, int index, string word)
{
    if (index == word.size())
        return true;
    if (r < 0 || r >= matrix.size() || c < 0 || c >= matrix[0].size() ||
        matrix[r][c] != word[index])
        return false;
    char tmp = word[index];
    matrix[r][c] = ' ';
    bool found;
    found = dfs(matrix, r + 1, c, index + 1, word) ||
            dfs(matrix, r, c + 1, index + 1, word) ||
            dfs(matrix, r - 1, c, index + 1, word) ||
            dfs(matrix, r, c - 1, index + 1, word);
    matrix[r][c] = tmp;
    return found;
}

/**
 * Time: O(n * 4**L) where L is the length of the word
 * Space: O(L)
 */
bool exist(vector<vector<char>> matrix, string word)
{
    for (int i = 0; i < matrix.size(); i++)
        for (int j = 0; j < matrix[0].size(); j++)
            if (matrix[i][j] == word[0] && dfs(matrix, i, j, 0, word))
                return true;
    return false;
}
