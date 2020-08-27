class Solution {
    enum Direction {
        LEFT, RIGHT
    }

    // Time: O(log(n))
    // Space: O(1)
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[] { -1, -1 };
        int left = bisect(nums, target, Direction.LEFT);
        if (left == nums.length || nums[left] != target) {
            return res;
        }
        res[0] = left;
        res[1] = bisect(nums, target, Direction.RIGHT) - 1;
        return res;
    }

    private int bisect(int[] nums, int target, Direction dir) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > target || (dir == Direction.LEFT && nums[mid] == target)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}