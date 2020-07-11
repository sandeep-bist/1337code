package main

// Time: O(n * 2**n)
// Space: O(n * 2**n)
func subsets(nums []int) [][]int {
	res := [][]int{}
	dfs(nums, 0, []int{}, &res)
	return res
}

func dfs(nums []int, index int, path []int, res *[][]int) {
	*res = append(*res, append([]int{}, path...))
	for i := index; i < len(nums); i++ {
		path := append(path, nums[i])
		dfs(nums, i+1, path, res)
		path = path[:len(path)-1]
	}
}

func main() {

}
