class Solution {
    // Time: O(n(log n))
    // Space: O(n)
    public String largestNumber(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return "";
        }
        String[] numbersAsStrings = new String[n];
        for (int i = 0; i < n; i++) {
            numbersAsStrings[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(numbersAsStrings, (a, b) -> (b + a).compareTo(a + b));
        if (numbersAsStrings[0].equals("0")) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(numbersAsStrings[i]);
        }
        return sb.toString();
    }

    public String largestNumberWithStreams(int[] nums) {
        return Arrays.stream(nums)
                     .mapToObj(Integer::toString)
                     .sorted((a, b) -> (b + a)
                     .compareTo(a + b))
                     .reduce((a, b) -> a + b)
                     .filter(str -> str.charAt(0) != '0')
                     .orElse("0");
    }
}