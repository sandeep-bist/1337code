package main

// Time: O(n)
// Space: O(n)
func findPermutation(s string) []int {
	res := make([]int, len(s)+1)
	for i := 1; i <= len(s)+1; i++ {
		res[i-1] = i
	}
	i := 0
	for i < len(s) {
		j := i + 1
		for j-1 < len(s) && s[j-1] == 'D' {
			j++
		}
		if j-i > 1 {
			swap(res, i, j-1)
		}
		i = j
	}
	return res
}

func swap(arr []int, i int, j int) {
	for i < j {
		arr[i], arr[j] = arr[j], arr[i]
		i++
		j--
	}
}

func main() {

}
