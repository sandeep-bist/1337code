package main

func findDuplicates(nums []int) []int {
	res := make([]int, 0)
	for _, num := range nums {
		index := abs(num) - 1
		if nums[index] < 0 {
			res = append(res, index+1)
		}
		nums[index] *= -1
	}
	return res
}

func abs(x int) int {
	if x < 0 {
		return x * -1
	}
	return x
}

func main() {

}
