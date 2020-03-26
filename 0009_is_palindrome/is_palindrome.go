package main

func isPalindrome(x int) bool {
	rev := 0
	if x < 0 || (x != 0 && x%10 == 0) {
		return false
	}
	for x > rev {
		rev = (rev * 10) + x%10
		x /= 10
	}
	return x == rev || x == (rev/10)
}

func main() {

}
