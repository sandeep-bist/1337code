package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func shortestDistance(words []string, word1 string, word2 string) int {
	m := len(words)
	i1, i2 := -1, -1
	for i, e := range words {
		if e == word1 {
			i1 = i
		} else if e == word2 {
			i2 = i
		}
		if i1 != -1 && i2 != -1 {
			m = min(abs(i1-i2), m)
		}
	}
	return m
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func main() {

}
