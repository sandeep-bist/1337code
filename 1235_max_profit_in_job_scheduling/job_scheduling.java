class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        // Time: O(n log n) + O(n log n)
        // Space: O(n)
        int[][] jobs = getSortedJobsByEndTime(startTime, endTime, profit);
        TreeMap<Integer, Integer> dp = new TreeMap<>();
        dp.put(0, 0);
        for (int[] job : jobs) {
            int s = job[0], e = job[1], p = job[2];
            int currProfit = getInsertPos(dp, s) + p;
            if (currProfit > dp.lastEntry().getValue())
                dp.put(e, currProfit);
        }
        return dp.lastEntry().getValue();
    }
    
    private int[][] getSortedJobsByEndTime(int[] start, int[] end, int[] profit) {
        int n = start.length;
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) {
            jobs[i] = new int[] {start[i], end[i], profit[i]};
        }
        Arrays.sort(jobs, (a, b) -> a[1] - b[1]);
        return jobs;
    }
    
    private int getInsertPos(TreeMap<Integer, Integer> map, int start) {
        return map.floorEntry(start).getValue();
    }
}