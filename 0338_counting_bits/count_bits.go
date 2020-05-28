package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func countBits(num int) []int {
    res := make([]int, num + 1)
    for i := 1; i <= num; i++ {
        res[i] = res[i & (i - 1)] + 1
    }
    return res
}

func main() {
	
}