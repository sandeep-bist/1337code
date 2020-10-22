interface ArrayReader {
    public int get(int index);
}

class Solution {
    // Time: O(log(t)) where t is the index of the targer
    // Space: O(1)
    public int search(ArrayReader reader, int target) {
        if (reader.get(0) == target) {
            return 0;
        }
        int left = 0, right = 1;
        while (reader.get(right) <= target) {
            left = right;
            right <<= 1;
        }
        while (left < right) {
            int mid = (left + right) / 2;
            int midVal = reader.get(mid);
            if (midVal == target) {
                return mid;
            }
            if (midVal > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}