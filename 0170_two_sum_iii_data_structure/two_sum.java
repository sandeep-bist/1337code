import java.util.Map;
import java.util.HashMap;

class TwoSum {

    Map<Integer, Integer> map;

    /** Initialize your data structure here. */
    public TwoSum() {
        map = new HashMap<Integer, Integer>();
    }

    /**
     * Add the number to an internal data structure.. Time: O(1)
     */
    public void add(int number) {
        if (map.containsKey(number)) {
            map.replace(number, map.get(number) + 1);
        } else {
            map.put(number, 1);
        }
    }

    /**
     * Find if there exists any pair of numbers which sum is equal to the value.
     * Time: O(1)
     */
    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int complement = value - entry.getKey();
            if (entry.getKey() == complement) {
                if (entry.getValue() > 1) {
                    return true;
                }
            } else {
                if (map.containsKey(complement)) {
                    return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such: TwoSum obj = new
 * TwoSum(); obj.add(number); boolean param_2 = obj.find(value);
 */