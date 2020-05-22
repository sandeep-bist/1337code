package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func frequencySort(s string) string {
	counter := map[rune]int{}
	for _, char := range s {
		counter[char]++
	}
	buckets := map[int][]rune{}
	maxFreq := 0
	for k, v := range counter {
		buckets[v] = append(buckets[v], k)
		if v > maxFreq {
			maxFreq = v
		}
	}
	var res []rune
	for ; maxFreq > 0; maxFreq-- {
		for _, v := range buckets[maxFreq] {
			for i := 0; i < maxFreq; i++ {
				res = append(res, v)
			}
		}
	}
	return string(res)
}
