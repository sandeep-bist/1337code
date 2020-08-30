// Time O(n * log(2m) * log(m)) where n is the number of elements
// and m is the max value in list
// Space: O(n + m)
class Solution {
    /**
     * Use union find to solve the problem: traverse all factors of each number in
     * array, union all numbers that contain same factors and then use a hashmap to
     * count number of elements in every disjoint set, find the max size
     */
    public int largestComponentSize(int[] A) {
        int maxVal = Arrays.stream(A).reduce(A[0], (x, y) -> x > y ? x : y);

        // initialize max value + 1 in array as size of parent array in union find,
        // since we need to at most
        // access the max value in union find class
        UnionFind unionFind = new UnionFind(maxVal + 1);
        for (int a : A) {
            for (int i = 2; i <= Math.sqrt(a); i++) {
                // if i is factor of a, union a, i, and a/i together
                if (a % i == 0) {
                    unionFind.union(a, i);
                    unionFind.union(a, a / i);
                }
            }
        }

        // traverse all elements in array, find their parents, iteratively count number
        // of elements in each
        // disjoint set
        int maxSize = 1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int a : A) {
            int parent = unionFind.find(a);
            map.put(parent, map.getOrDefault(parent, 0) + 1);
            maxSize = Math.max(maxSize, map.get(parent));
        }
        return maxSize;
    }
}

class UnionFind {
    int[] parent;

    public UnionFind(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    public void union(int x, int y) {
        parent[find(x)] = parent[find(y)];
    }

    public int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}