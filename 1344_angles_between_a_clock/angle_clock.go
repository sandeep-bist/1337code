package main

import "math"

// Time: O(1)
// Space: O(1)
func angleClock(hour int, minutes int) float64 {
	var h, m float64
	h = float64(30*hour) + float64(minutes/2)
	m = 6 * float64(minutes)
	diff := math.Abs(h - m)
	return math.Min(diff, 360-diff)
}

func main() {

}
