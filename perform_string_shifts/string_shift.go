package main

import "strings"

/**
 * Time: O(n)
 * Space: O(n)
 */
func stringShift(s string, shift [][]int) string {
	var res []string
	var count int
	for _, cmd := range shift {
		if cmd[0] == 0 {
			count -= cmd[1]
		} else {
			count += cmd[1]
		}
	}
	count %= len(s)
	offset := 0 - count
	if count > 0 {
		offset = len(s) - count
	}
	res = append(res, s[offset:], s[:offset])
	return strings.Join(res, "")
}

func main() {

}
