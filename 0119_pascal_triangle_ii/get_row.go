package main

// Time: O(n**2)
// Space: O(n)
func getRow(rowIndex int) []int {
	res := []int{1}
	for i := 1; i < rowIndex+1; i++ {
		for j := len(res) - 1; j > 0; j-- {
			res[j] += res[j-1]
		}
		res = append(res, 1)
	}
	return res
}

func main() {

}
