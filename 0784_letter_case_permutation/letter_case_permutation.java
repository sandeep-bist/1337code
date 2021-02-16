class Solution {
    // Time: O(2**n)
    // Space: O(n)
    public List<String> letterCasePermutation(String S) {
        List<String> res = new ArrayList<String>();
        dfs(0, S.toCharArray(), res);
        return res;
    }
    
    private void dfs(int index, char[] curr, List<String> res) {
        if (index == curr.length) {
            res.add(new String(curr));
            return;
        }
        if (Character.isLetter(curr[index])) {
            curr[index] = Character.toLowerCase(curr[index]);
            dfs(index + 1, curr, res);
            curr[index] = Character.toUpperCase(curr[index]);
            dfs(index + 1, curr, res);
        } else {
            dfs(index + 1, curr, res);    
        }       
    }
}