package main

func counter(A []int) map[int]int {
	c := make(map[int]int)
	for i := 0; i < len(A); i++ {
		curr := A[i]
		_, ok := c[curr]
		if ok {
			c[curr]++
		} else {
			c[curr] = 1
		}
	}
	return c
}

// Time: O(n)
// Space: O(n)
func largestUniqueNumber(arr []int) int {
	c := counter(arr)
	maxUniq := -1
	for k, v := range c {
		if v == 1 && k > maxUniq {
			maxUniq = k
		}
	}
	return maxUniq
}
