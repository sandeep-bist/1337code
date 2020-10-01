import java.util.LinkedList;

class RecentCounter {

    LinkedList<Integer> window;

    public RecentCounter() {
        window = new LinkedList<>();
    }

    public int ping(int t) {
        window.addLast(t);
        while (window.size() > 0) {
            if (t - 3000 > window.getFirst()) {
                window.removeFirst();
            } else {
                break;
            }
        }
        return window.size();
    }
}
