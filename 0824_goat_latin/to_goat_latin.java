class Solution {
    public String toGoatLatin(String S) {
        Set<Character> vowels = new HashSet<>();
        for (char c : "aeiouAEIOU".toCharArray())
            vowels.add(c);
        String suffix = "";
        StringBuilder sb = new StringBuilder();
        for (String s : S.split(" ")) {
            suffix += 'a'; // Java compiler converts this into a temporary StringBuilder
            if (!vowels.contains(s.charAt(0))) {
                s = s.substring(1) + s.charAt(0);
            }
            sb.append(s).append("ma").append(suffix).append(' ');
        }
        sb.deleteCharAt(sb.length() - 1); // remove extra space
        return sb.toString();
    }
}