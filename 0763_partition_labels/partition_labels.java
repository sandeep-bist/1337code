class Solution {
    // Time: O(n)
    // Space: O(1)
    public List<Integer> partitionLabels(String S) {
        int size = S.length();
        int[] lastIndex = new int[26];
        for (int i = 0; i < size; i++) {
            lastIndex[S.charAt(i) - 'a'] = i;
        }
        List<Integer> res = new ArrayList<Integer>();
        int j = 0, anchor = 0;
        for (int i = 0; i < size; i++) {
            j = Math.max(lastIndex[S.charAt(i) - 'a'], j);
            if (i == j) {
                res.add(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return res;
    }
}