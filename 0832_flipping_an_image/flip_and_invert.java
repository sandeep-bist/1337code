class Solution {
    // Time: O(n**2)
    // Space: O(n**2)
    public int[][] flipAndInvertImage(int[][] A) {
        if(A==null || A.length ==0)
            return A;   
        for(int[] row : A){
            for(int i = 0, j = row.length - 1; i <= j; i++, j--) {
                int temp = row[i];
                row[i]= 1 - row[j];
                row[j]= 1 - temp;
            }
        }
        return A;
    }
}