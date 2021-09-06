class Solution {
    // Time: O(n)
    // Space: O(1)
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int maxTime = releaseTimes[0];
        char maxChar = keysPressed.charAt(0);
        for (int i = 1; i < releaseTimes.length; i++) {
            int currTime = releaseTimes[i] - releaseTimes[i - 1];
            char currChar = keysPressed.charAt(i);
            if (currTime > maxTime || (currTime == maxTime && currChar > maxChar)) {
                maxTime = currTime;
                maxChar = currChar;
            }
        }
        return maxChar;
    }
}