class CombinationIterator {
    public Deque<String> combinations = new ArrayDeque<String>();

    // Time: O(2**n * n)
    // Space: O(k * C**k)
    public CombinationIterator(String characters, int combinationLength) {
        int n = characters.length();
        int k = combinationLength;

        for (int bitmask = 0; bitmask < 1 << n; bitmask++) {
            if (Integer.bitCount(bitmask) == k) {
                StringBuilder curr = new StringBuilder();
                for (int j = 0; j < n; j++) {
                    if ((bitmask & (1 << n - j - 1)) != 0)
                        curr.append(characters.charAt(j));
                }
                combinations.push(curr.toString());
            }
        }
    }

    // Time: O(1)
    public String next() {
        return combinations.pop();
    }

    public boolean hasNext() {
        return (!combinations.isEmpty());
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters,
 * combinationLength); String param_1 = obj.next(); boolean param_2 =
 * obj.hasNext();
 */