class MovingAverage {

    private Queue<Integer> q;
    private double total;
    private int max_size;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        q = new LinkedList<Integer>();
        max_size = size;
    }

    // Time: O(1)
    // Space: O(1)
    public double next(int val) {
        if (q.size() == max_size) {
            total -= q.poll();
        }
        total += val;
        q.offer(val);
        return total / q.size();
    }
}
