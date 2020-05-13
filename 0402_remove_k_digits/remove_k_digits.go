package main

import "strconv"

/**
 * Time: O(n)
 * Space: O(n)
 */
func removeKdigits(num string, k int) string {
	numStack := make([]int, 1)
	for _, n := range num {
		for k != 0 && len(numStack) != 0 && numStack[len(numStack)-1] > int(n-'0') {
			k--
			numStack = numStack[:len(numStack)-1]
		}
		numStack = append(numStack, int(n-'0'))
	}
	for k != 0 {
		numStack = numStack[:len(numStack)-1]
		k--
	}
	res := ""
	flag := false
	for _, i := range numStack {
		if i > 0 {
			flag = true
		}
		if flag {
			res += strconv.Itoa(i)
		}
	}
	if res == "" {
		return "0"
	}
	return res
}

func main() {

}
