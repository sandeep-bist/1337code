#include <stdio.h>

/**
 * Given a sorted array nums, remove the duplicates in-place such that 
 * duplicates appeared at most twice and return the new length.
 * Do not allocate extra space for another array, you must do this by
 * modifying the input array in-place with O(1) extra memory. 
 */
int removeDuplicates(int *nums, int numsSize)
{
    int i = 0, j;
    for (j = 0; j < numsSize; j++)
        if (i < 2 || nums[i - 2] < nums[j])
            nums[i++] = nums[j];
    return i;
}

int main()
{
    int arr[] = {1, 1, 1, 2, 2, 3};
    int size = sizeof(arr) / sizeof(int);
    printf("%i\n", removeDuplicates(arr, size)); // 5
}