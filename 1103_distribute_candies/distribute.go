package main

// Time: O(n)
// Space: O(n)
func distributeCandies(candies int, num_people int) []int {
	res := make([]int, num_people)
	index, count := 0, 1
	for candies > 0 {
		if count < candies {
			res[index%num_people] += count
		} else {
			res[index%num_people] += candies
		}
		candies -= count
		count++
		index++
	}
	return res
}

func main() {

}
