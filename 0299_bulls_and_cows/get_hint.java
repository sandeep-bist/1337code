import java.util.HashMap;

class Solution {
    // Time: O(n)
    // Space: O(n)
    public String getHint(String secret, String guess) {
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        int bulls = 0, cows = 0;
        for (int i = 0; i < secret.length(); i++) {
            char s = secret.charAt(i);
            char g = guess.charAt(i);
            if (s == g) {
                bulls++;
            } else {
                if (hm.getOrDefault(s, 0) < 0) {
                    cows++;
                }
                if (hm.getOrDefault(g, 0) > 0) {
                    cows++;
                }
                hm.put(s, hm.getOrDefault(s, 0) + 1);
                hm.put(g, hm.getOrDefault(g, 0) - 1);
                System.out.println(hm);
            }
        }
        return Integer.toString(bulls) + "A" + Integer.toString(cows) + "B";
    }
}