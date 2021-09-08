class Solution {
    // Time: O(n)
    // Space: O(n)
    public String shiftingLetters(String s, int[] shifts) {
        StringBuilder res = new StringBuilder(s);
        for (int i = shifts.length - 2; i >= 0; i--) {
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26;
        }
        for (int i = 0; i < s.length(); i++) {
            char shiftedChar = shiftCharByIndexes(s.charAt(i), shifts[i]);
            res.setCharAt(i, shiftedChar);
        }
        return res.toString();
    }
    
    private char shiftCharByIndexes(char c, int numOfIndexes) {
        return (char)((c - 'a' + numOfIndexes) % 26 + 'a');
    }
}