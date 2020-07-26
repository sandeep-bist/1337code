package main

// Time: O(1)
// Space: O(1)
func addDigits(num int) int {
	if num == 0 {
		return 0
	}
	return 1 + (num-1)%9
}

func main() {

}
