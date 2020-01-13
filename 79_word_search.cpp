#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 * Depth-first search.
 */
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
 * Given a 2D board and a word, find if the word exists in the grid.
 * The word can be constructed from letters of sequentially adjacent cell,
 * where "adjacent" cells are those horizontally or vertically neighboring.
 * The same letter cell may not be used more than once.
 */
bool exist(vector<vector<char>> matrix, string word)
{
    for (int i = 0; i < matrix.size(); i++)
        for (int j = 0; j < matrix[0].size(); j++)
            if (matrix[i][j] == word[0] && dfs(matrix, i, j, 0, word))
                return true;
    return false;
}

int main()
{
    vector<vector<char>> matrix{
        {'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    cout << exist(matrix, "ABCCED") << endl; // 1
    cout << exist(matrix, "ABCD") << endl;   // 0
    return 0;
}