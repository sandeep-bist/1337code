// Time: O(n**2)
// Space: O(n**2)
class Solution {
    public List<List<Integer>> generate(int numRows) {
        var res = new ArrayList<List<Integer>>();
        if (numRows == 0)
            return res;
        res.add(new ArrayList<Integer>());
        res.get(0).add(1);
        for (int i = 1; i < numRows; i++) {
            var tmp = new ArrayList<Integer>();
            tmp.add(1);
            for (int j = 1; j < i; j++)
                tmp.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
            tmp.add(1);
            res.add(tmp);
        }
        return res;
    }
}