package main

// Time: O(n)
// Space: O(1)
func longestPalindrome(s string) int {
	count := [128]int{}
	res := 0
	for i := 0; i < len(s); i++ {
		char := s[i]
		count[char]++
		if count[char] == 2 {
			res += 2
			count[char] = 0
		}
	}
	if res == len(s) {
		return res
	}
	return res + 1
}

func main() {

}
