package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func countElements(arr []int) int {
	s := make(map[int]bool)
	for _, i := range arr {
		s[i] = true
	}
	count := 0
	for _, i := range arr {
		if s[i+1] == true {
			count++
		}
	}
	return count
}

func main() {

}
