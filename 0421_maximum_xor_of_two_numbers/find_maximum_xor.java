class Solution {
    class Trie {
        Trie[] children;

        public Trie() {
            children = new Trie[2];
        }
    }

    public int findMaximumXOR(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        Trie root = new Trie();
        for (int num : nums) {
            Trie currNode = root;
            for (int i = 31; i >= 0; i--) {
                int currBit = (num >> i) & 1;
                if (currNode.children[currBit] == null) {
                    currNode.children[currBit] = new Trie();
                }
                currNode = currNode.children[currBit];
            }
        }
        int res = Integer.MIN_VALUE;
        for (int num : nums) {
            Trie currNode = root;
            int currSum = 0;
            for (int i = 31; i >= 0; i--) {
                int currBit = (num >> i) & 1;
                if (currNode.children[currBit ^ 1] != null) {
                    currSum += (1 << i);
                    currNode = currNode.children[currBit ^ 1];
                } else {
                    currNode = currNode.children[currBit];
                }
            }
            res = Math.max(currSum, res);
        }
        return res;
    }
}