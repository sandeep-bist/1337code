package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func checkStraightLine(coordinates [][]int) bool {
	x0, x1, y0, y1 := coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]
	dx, dy := x1-x0, y1-y0
	// slope is dx / dy
	for _, coord := range coordinates {
		x, y := coord[0], coord[1]
		if (x-x1)*dy != (y-y1)*dx {
			return false
		}
	}
	return true
}

func main() {

}
