// Time: O(log(n))
// Space: O(1)
func myPow(x float64, n int) float64 {
	var res float64
	res = 1
	tmp := abs(n)
	for tmp != 0 {
		if tmp&1 == 1 {
			res *= x
		}
		x *= x
		tmp >>= 1
	}
	if n > 0 {
		return res
	}
	return 1 / res
}

func abs(x int) int {
	if x < 0 {
		return x * -1
	}
	return x
}