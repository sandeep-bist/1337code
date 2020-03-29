package main

// Time: O(n)
// Space: O(1)
func validPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			i1, j1 := i, j-1
			i2, j2 := i+1, j
			for i1 < j1 && s[i1] == s[j1] {
				i1++
				j1--
			}
			for i2 < j2 && s[i2] == s[j2] {
				i2++
				j2--
			}
			return i1 >= j1 || i2 >= j2
		}
	}
	return true
}

func main() {

}
