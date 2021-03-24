class Solution {
    // Time: O(n)
    // Space: O(n)
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>();
        LinkedHashMap<Integer, String> hashMap = new LinkedHashMap<Integer, String>() {
            {
                put(3, "Fizz");
                put(5, "Buzz");
            }
        };
        for (int i = 1; i <= n; i++) {
            String tmp = "";
            for (Integer key : hashMap.keySet()) {
                if (i % key == 0) {
                    tmp += hashMap.get(key);
                }
            };
            if (tmp == "") {
                tmp += Integer.toString(i);
            }
            res.add(tmp);
        }
        return res;
    }
}