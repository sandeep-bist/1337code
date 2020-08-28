/**
 * The rand7() API is already defined in the parent class SolBase. public int
 * rand7();
 * 
 * @return a random integer in the range 1 to 7
 */

// Time: O(1) - O(infinity)
// Space: O(1)
class Solution extends SolBase {
    // Average calls = 2.45
    public int rand10() {
        int rand40 = 40;
        while (rand40 >= 40) {
            rand40 = (rand7() - 1) * 7 + rand7() - 1;
        }
        return rand40 % 10 + 1;
    }

    Stack<Integer> cache = new Stack<Integer>();

    // Average calls = 1.199
    public int rand10withCache() {
        while (cache.empty())
            generate();
        return cache.pop();
    }

    void generate() {
        int n = 19;
        long cur = 0, range = (long) Math.pow(7, n);
        for (int i = 0; i < n; ++i) {
            cur += (long) Math.pow(7, i) * (rand7() - 1);
        }
        while (cur < range / 10 * 10) {
            cache.push((int) (cur % 10 + 1));
            cur /= 10;
            range /= 10;
        }
    }
}