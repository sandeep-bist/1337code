// Time: O(n)
// Space: O(1)
func plusOne(digits []int) []int {
	carry := 1
	for i := len(digits) - 1; i >= 0; i-- {
		curr := digits[i] + carry
		carry = curr / 10
		digits[i] = curr % 10
	}
	if carry == 1 {
		return append([]int{1}, digits...)
	}
	return digits
}