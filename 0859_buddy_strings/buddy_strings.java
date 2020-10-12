import java.util.*;

class Solution {
    // Time: O(n)
    // Space: O(1)
    public boolean buddyStrings(String A, String B) {
        if (A.length() != B.length()) {
            return false;
        }
        if (A.equals(B)) {
            Set<Character> seen = new HashSet<Character>();
            for (char c : A.toCharArray()) {
                seen.add(c);
            }
            return seen.size() != A.length();
        } else {
            List<Integer> diff = new ArrayList<>();
            for (int i = 0; i < A.length(); i++) {
                if (A.charAt(i) != B.charAt(i)) {
                    diff.add(i);
                }
            }
            return diff.size() == 2 && A.charAt(diff.get(0)) == B.charAt(diff.get(1))
                    && A.charAt(diff.get(1)) == B.charAt(diff.get(0));
        }
    }
}