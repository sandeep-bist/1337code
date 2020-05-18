package main

/**
 * Time: O(s + p)
 * Space: O(p)
 */
func findAnagrams(s string, p string) []int {
	pCount := make(map[byte]int)
	counter := len(p)
	result := make([]int, 0)
	for i := 0; i < len(p); i++ {
		pCount[p[i]]++
	}
	begin, end := 0, 0
	for end < len(s) {
		val := pCount[s[end]]
		pCount[s[end]]--
		if val > 0 {
			counter--
		}
		end++
		if counter == 0 {
			result = append(result, begin)
		}
		if end >= len(p) {
			val := pCount[s[begin]]
			pCount[s[begin]]++
			if val >= 0 {
				counter++
			}
			begin++
		}
	}
	return result
}

func main() {

}
