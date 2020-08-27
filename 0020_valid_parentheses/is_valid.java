class Solution {
    // Time: O(n)
    // Space: O(n)
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> hashMap = new HashMap<Character, Character>() {
            {
                put('(', ')');
                put('[', ']');
                put('{', '}');
            }  
        };
        for (char c: s.toCharArray()) {
            if (hashMap.containsKey(c)) {
                stack.add(c);
                continue;
            }
            if (stack.isEmpty())
                return false;
            char tmp = stack.pop();
            char compliment = hashMap.get(tmp);
            if (c != compliment)
                return false;
        }
        return stack.isEmpty();
    }
}