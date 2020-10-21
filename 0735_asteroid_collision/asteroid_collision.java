import java.util.LinkedList;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        LinkedList<Integer> res = new LinkedList<>();
        for (int a : asteroids) {
            if (a > 0) {
                res.add(a);
            } else {
                while (!res.isEmpty() && res.getLast() > 0 && res.getLast() < -a) {
                    res.pollLast();
                }
                if (!res.isEmpty() && res.getLast() == -a) {
                    res.pollLast();
                } else if (res.isEmpty() || res.getLast() < 0) {
                    res.add(a);
                }
            }
        }
        return res.stream().mapToInt(i -> i).toArray();
    }
}