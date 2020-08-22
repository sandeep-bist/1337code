class Solution {
    int[][] rects;
    List<Integer> sums = new ArrayList<>();
    int total = 0;
    Random rand = new Random();

    // Time: O(n)
    // Space: O(n)
    public Solution(int[][] rects) {
        this.rects = rects;
        for (int[] x : rects) {
            total += (x[2] - x[0] + 1) * (x[3] - x[1] + 1);
            sums.add(total);
        }
    }

    // Time: O(log(n))
    // Space: O(1)
    public int[] pick() {
        int target = rand.nextInt(total);
        int index = binarySearch(target);
        int[] x = rects[index];
        int width = x[2] - x[0] + 1;
        int height = x[3] - x[1] + 1;
        int base = sums.get(index) - width * height;
        return new int[] { x[0] + (target - base) % width, x[1] + (target - base) / width };
    }

    private int binarySearch(int target) {
        int lo = 0, hi = rects.length - 1;
        while (lo != hi) {
            int mid = (lo + hi) / 2;
            if (target >= sums.get(mid)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}