class Solution {
    // Time: O(n)
    // Space: O(1)
    public String reverseOnlyLetters(String S) {
        StringBuilder sb = new StringBuilder(S);
        int i = 0, j = S.length() - 1;
        while (i < j) {
            while (i < j && !Character.isLetter(sb.charAt(i))) {
                i++;
            }
            while (i < j && !Character.isLetter(sb.charAt(j))) {
                j--;
            }
            char tmp = sb.charAt(i);
            sb.setCharAt(i++, S.charAt(j));
            sb.setCharAt(j--, tmp);
        }
        return sb.toString();
    }
}