package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func numJewelsInStones(J string, S string) int {
    jewels := make(map[rune]bool)
    for _, j := range(J) {
        jewels[j] = true
    }
    res := 0
    for _, s := range(S) {
        _, ok := jewels[s]
        if ok {
            res++
        }
    }
    return res
}

func main() {

}