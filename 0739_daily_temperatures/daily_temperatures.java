class Solution {
    // Time: O(n)
    // Space: O(n)
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int currDay = 0; currDay < n; currDay++) {
            int currTemp = temperatures[currDay];
            while (!stack.isEmpty() && currTemp > temperatures[stack.peek()]) {
                int prevDay = stack.pop();
                res[prevDay] = currDay - prevDay;
            }
            stack.push(currDay);
        }
        return res;
    }
}