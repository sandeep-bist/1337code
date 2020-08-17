// Time: O(n)
// Space: O(n)
class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] res = new int[num_people];
        int count = 1, i = 0;
        while (candies > 0) {
            res[i++] += (count <= candies) ? count : candies;
            candies -= count++;
            if (i >= num_people)
                i = 0;
        }
        return res;
    }
}