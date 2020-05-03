package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func canConstruct(ransomNote string, magazine string) bool {
	m := make([]int, 26, 26)
	for i := 0; i < len(magazine); i++ {
		m[int(magazine[i])-int('a')]++
	}
	for j := 0; j < len(ransomNote); j++ {
		m[int(ransomNote[j])-int('a')]--
		if m[int(ransomNote[j])-int('a')] < 0 {
			return false
		}
	}
	return true
}

func main() {

}
