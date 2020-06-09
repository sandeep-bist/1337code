package main

/**
 * Time: O(m + n)
 * Space: O(m + n)
 */
func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}
	i := 0
	for _, c := range t {
		if c == rune(s[i]) {
			i++
		}
		if i == len(s) {
			return true
		}
	}
	return false
}

func main() {

}
