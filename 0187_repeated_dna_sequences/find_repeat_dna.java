import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int L = 10, n = s.length();
        HashSet<String> seen = new HashSet(), output = new HashSet();

        for (int i = 0; i < n - L + 1; i++) {
            String tmp = s.substring(i, i + L);
            if (seen.contains(tmp)) {
                output.add(tmp);
            }
            seen.add(tmp);
        }
        return new ArrayList<String>(output);
    }
}