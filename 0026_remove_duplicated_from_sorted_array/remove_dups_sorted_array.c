#include <stdio.h>

/**
 * Time: O(n)
 * Space: O(1)
 */
int remove_duplicates(int *nums, int numsSize)
{
    int i = 0, j;
    for (j = 0; j < numsSize; j++)
        if (i < 1 || nums[i - 1] < nums[j])
            nums[i++] = nums[j];
    return i;
}
