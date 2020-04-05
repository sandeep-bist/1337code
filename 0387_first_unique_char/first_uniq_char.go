package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func firstUniqChar(s string) int {
	res := make([]int, 26)
	for i := 0; i < len(s); i++ {
		res[s[i]-'a']++
	}
	for i := 0; i < len(s); i++ {
		if res[s[i]-'a'] == 1 {
			return i
		}
	}
	return -1
}

func main() {

}
