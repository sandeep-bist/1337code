// Time: O(n)
// Space: O(n)
class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        int[] bucket = new int[len + 1];
        for (int c : citations)
            if (c > len)
                bucket[len]++;
            else
                bucket[c]++;
        int res = 0;
        for (int i = len; i >= 0; i--) {
            res += bucket[i];
            if (res >= i)
                return i;
        }
        return 0;
    }
}