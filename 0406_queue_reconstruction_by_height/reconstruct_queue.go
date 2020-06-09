package main

import "sort"

/**
 * Time: O(n**2)
 * Space: O(n)
 */
func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] > people[j][0] {
			return true
		}
		if people[i][0] == people[j][0] && people[i][1] < people[j][1] {
			return true
		}
		return false
	})
	res := make([][]int, len(people))
	for i := 0; i < len(people); i++ {
		p := people[i][1]
		copy(res[p+1:], res[p:])
		res[p] = people[i]
	}
	return res
}

func main() {

}
