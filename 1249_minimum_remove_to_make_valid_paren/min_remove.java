class Solution {
    // Time: O(n)
    // Space: O(n)
    public String minRemoveToMakeValid(String s) {
        char[] str = s.toCharArray();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < str.length; i++) {
            if (str[i] == '(') {
                stack.push(i);
            } else if (str[i] == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    str[i] = '*';
                }
            }
        }
        while (!stack.isEmpty()) {
            str[stack.pop()] = '*';
        }
        return new String(str).replaceAll("\\*", "");
    }
}