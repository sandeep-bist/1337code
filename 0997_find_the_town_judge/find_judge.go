package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func findJudge(N int, trust [][]int) int {
    votes := make([]int, N + 1)
    for _, item := range(trust) {
        votes[item[0]]--
        votes[item[1]]++
    }
    for i := 1; i < N + 1; i++ {
        if votes[i] == N - 1 {
            return i
        }
    }
    return -1
}

func main() {

}