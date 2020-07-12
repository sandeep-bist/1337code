package main

func reverseBits(num uint32) uint32 {
	res := uint32(0)
	i := uint32(31)
	for num != 0 {
		res += (num & 1) << i
		num >>= 1
		i--
	}
	return res
}

func main() {

}
