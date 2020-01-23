package main

import "fmt"

// Returns the absolute value of an integer.
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
// elements appear twice and others appear once. Find all the elements of
// [1, n] inclusive that do not appear in this array.
// O(n) time complexity, O(1) space complexity.
func findDisappearedNumbers(nums []int) []int {
    res := []int{}
    for i := range(nums) {
        index := abs(nums[i]) - 1
        if nums[index] > 0 {
            nums[index] *= -1
        }
    }
    for i := range(nums) {
        if nums[i] > 0 {
            res = append(res, i + 1)
        }
    }
    return res
}

func main() {
    arr := []int{4, 3, 2, 7, 8, 2, 3, 1}
    fmt.Println(findDisappearedNumbers(arr)) // [5 6]
}