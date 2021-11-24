class Solution {
    // Time: O(n)
    // Space: O(n)
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0, j = 0;
        List<int[]> result = new ArrayList<>();
        while (i < firstList.length && j < secondList.length) {
            int[] first = firstList[i];
            int[] second = secondList[j];
            int start = Math.max(first[0], second[0]);
            int end = Math.min(first[1], second[1]);
            if (start <= end) {
                result.add(new int[] {start, end});
            }
            if (first[1] < second[1]) {
                i++;
            } else {
                j++;
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}