class Solution {
    // Time: O(n)
    // Space: O(n)
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for (String email : emails) {
            String[] parts = email.split("@");
            String[] local = parts[0].split("\\+");
            set.add(local[0].replace(".", "") + "@" + parts[1]);      
        }
        return set.size();
    }
}