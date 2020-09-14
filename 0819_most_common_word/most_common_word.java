import java.util.Set;
import java.util.HashSet;

class Solution {
    // Time: O(m + n)
    // Space: O(m + n)
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banSet = new HashSet<>(Arrays.asList(banned));
        return Arrays.asList(paragraph.replaceAll("[!?',;.]", " ")
            .toLowerCase()
            .split("\\s+"))
            .stream()
            .filter(word -> !banSet.contains(word))
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
            .entrySet()
            .stream()
            .max(Map.Entry.comparingByValue())
            .get()
            .getKey();
    }
}