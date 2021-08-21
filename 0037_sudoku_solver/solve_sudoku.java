public class Solution {
    // Time: O(9**n) where n is the number of empty cells
    // Space: O(m * n)
    public void solveSudoku(char[][] board) {
        if (board == null || board.length == 0)
            return;
        solve(board);
    }
    
    private boolean solve(char[][] board){
        int n = board.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != '.') {
                    continue;
                }
                return tryNumbers(board, i, j);
            }
        }
        return true;
    }
    
    private boolean tryNumbers(char[][] board, int row, int col) {
        for (char c = '1'; c <= '9'; c++){
            if (isValidPosition(board, row, col, c)) {
                board[row][col] = c;
                if (solve(board)) {
                    return true; 
                }
                board[row][col] = '.';
            }
        }
        return false;
    }
    
    private boolean isValidPosition(char[][] board, int row, int col, char c){
        return isValidRow(board, row, c) && 
               isValidCol(board, col, c) &&
               isValidSquare(board, row, col, c);
    }
    
    private boolean isValidRow(char[][] board, int row, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c) {
                return false;
            }
        }
        return true;
    }
    
    private boolean isValidCol(char[][] board, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) {
                return false;
            }
        }
        return true;
    }
    
    private boolean isValidSquare(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) {
                return false;
            }
        }
        return true;
    }
}
