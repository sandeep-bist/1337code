package main

/**
 * Time: O(s1 + s2)
 * Space: O(s1)
 */
func checkInclusion(s1 string, s2 string) bool {
	s1Count := make(map[byte]int)
	counter := len(s1)
	for _, c := range s1 {
		s1Count[byte(c)]++
	}
	begin, end := 0, 0
	for end < len(s2) {
		val := s1Count[s2[end]]
		s1Count[s2[end]]--
		if val > 0 {
			counter--
		}
		end++
		if counter == 0 {
			return true
		}
		if end >= len(s1) {
			val := s1Count[s2[begin]]
			s1Count[s2[begin]]++
			if val >= 0 {
				counter++
			}
			begin++
		}
	}
	return counter == 0
}

func main() {

}
