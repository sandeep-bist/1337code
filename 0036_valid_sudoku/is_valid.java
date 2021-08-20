public class Solution {
    // Time: O(n**2)
    // Space: O(n**2)
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        boolean[][] row = new boolean[n][n];
        boolean[][] col = new boolean[n][n];
        boolean[][] square = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int pos = board[i][j] - '1';
                if (row[i][pos] || col[j][pos] || square[getSquareIndex(i, j)][pos]) {
                    return false;
                }
                row[i][pos] = col[j][pos] = square[getSquareIndex(i, j)][pos] = true;
            }
        }
        return true;
    }

    private int getSquareIndex(int i, int j) {
        return (i / 3) * 3 + j / 3;
    }
}
