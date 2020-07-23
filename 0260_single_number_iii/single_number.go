package main

func singleNumber(nums []int) []int {
	xor := 0
	for _, v := range nums {
		xor = xor ^ v
	}
	lastBit := xor & (-xor)
	res := make([]int, 2)
	for _, v := range nums {
		if v&lastBit == 0 {
			res[0] ^= v
		} else {
			res[1] ^= v
		}
	}
	return res
}

func main() {

}
