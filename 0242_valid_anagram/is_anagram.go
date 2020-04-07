package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	alphabet := make([]int, 26)
	for i := 0; i < len(s); i++ {
		alphabet[s[i]-'a']++
		alphabet[t[i]-'a']--
	}
	for i := 0; i < 26; i++ {
		if alphabet[i] > 0 {
			return false
		}
	}
	return true
}

func main() {

}
