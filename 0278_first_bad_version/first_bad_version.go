package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

/**
 * Time: O(n * log(n))
 * Space: O(1)
 */
func firstBadVersion(n int) int {
	start, end := 0, n-1
	for start <= end {
		mid := (start + end) / 2
		if isBadVersion(mid) == true {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return start
}

func main() {
	
}