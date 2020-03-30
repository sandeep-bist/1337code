package main

import "strconv"

// Time: O(m + n)
// Space: O(n)
func addStrings(num1 string, num2 string) string {
	i, j := len(num1)-1, len(num2)-1
	res, carry := "", 0
	for i >= 0 || j >= 0 || carry > 0 {
		if i >= 0 {
			carry += int(num1[i] - '0')
			i--
		}
		if j >= 0 {
			carry += int(num2[j] - '0')
			j--
		}
		// prepends string
		res = strconv.Itoa(carry%10) + res
		carry /= 10
	}
	return res
}

func main() {

}
