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
	begin := 0
	end := 0
	for end < len(s) {
		val, ok := pCount[s[end]]
		if ok {
			pCount[s[end]]--
			if val > 0 {
				counter--
			}
		}
		end++
		if counter == 0 {
			result = append(result, begin)
		}
		if end >= len(p) {
			val, ok := pCount[s[begin]]
			if ok {
				pCount[s[begin]]++
				if val >= 0 {
					counter++
				}
			}
			begin++
		}
	}
	return result
}

func main() {

}
