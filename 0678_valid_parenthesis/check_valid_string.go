package main

/**
 * Time: O(n) 
 * Space: O(1)
 */
func checkValidString(s string) bool {
	var curr_min, curr_max int
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			curr_min++
			curr_max+++
		} else if s[i] == ')' {
			curr_max--
			curr_min = max(curr_min-1, 0)
		} else {
			curr_max++
			curr_min = max(curr_min-1, 0)
		}
		if curr_max < 0 {
			return false
		}
	}
	return curr_min == 0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}