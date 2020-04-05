package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func countPrimes(n int) int {
	if n <= 2 {
		return 0
	}
	res := 1
	primes := make([]int, n)
	for i := 3; i < n; i += 2 {
		if primes[i] == 0 {
			res++
			for j := i * i; j < n; j += i {
				primes[j] = 1
			}
		}
	}
	return res
}

func main() {

}
