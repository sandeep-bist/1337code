import java.lang.StringBuilder;

public class Solution {
    // Time: O(n)
    // Space: O(n)
    public String reverseWords(String s) {
        String[] split = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        reverse(split);
        for (int k = 0; k < split.length; k++) {
            sb.append(split[k] + " ");
        }
        return sb.toString().trim();
    }

    private void reverse(String[] stringArray) {
        int i = 0, j = stringArray.length - 1;
        while (i < j) {
            String tmp = stringArray[i];
            stringArray[i] = stringArray[j];
            stringArray[j] = tmp;
            i++;
            j--;
        }
    }
}

class reverse_words {

}
