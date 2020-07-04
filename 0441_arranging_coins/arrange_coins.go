package main

// Time: O(log(n))
// Space: O(1)
func arrangeCoins(n int) int {
	i, j := 0, n
	for i <= j {
		mid := (i + j) / 2
		k := mid * (mid + 1) / 2
		if k == n {
			return mid
		} else if k > n {
			j = mid - 1
		} else {
			i = mid + 1
		}
	}
	return j
}

func main() {

}
