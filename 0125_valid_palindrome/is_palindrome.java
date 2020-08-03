class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                i++;
                continue;
            } else if (!Character.isLetterOrDigit(s.charAt(j))) {
                j--;
                continue;
            }
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    /** An alternate solution using Java 8 Streams */
    public boolean isPalindromeUsingStreams(String s) {
        StringBuilder builder = new StringBuilder();

        s.chars().filter(c -> Character.isLetterOrDigit(c)).mapToObj(c -> Character.toLowerCase((char) c))
                .forEach(builder::append);

        return builder.toString().equals(builder.reverse().toString());
    }
}
