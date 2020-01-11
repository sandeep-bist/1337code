// Returns a counter of all elements in a integer array.
func counter(A []int) map[int]int {
    c := make(map[int]int)
    for i := 0; i < len(A); i++ {
        curr := A[i]
        _, ok := c[curr]
        if ok {
            c[curr]++
        } else {
            c[curr] = 1
        }
    }
    return c
}

// Given an array of integers arr, return the largest integer that only
// occurs once.
// If no integer occurs once, return -1.
func largestUniqueNumber(arr []int) int {
    c := counter(arr)
    max_uniq := -1
    for k, v := range(c) {
        if v == 1 && k > max_uniq {
            max_uniq = k
        }     
    }
    return max_uniq
}

func main {
	arr := []int{5,7,3,9,4,9,8,3,1}
    fmt.Println(largestUniqueNumber(arr))
}