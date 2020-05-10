package main

/**
 * Time: O(log(n))
 * Space: O(1)
 */
func isPerfectSquare(num int) bool {
    if num < 2 {
        return true
    }
    l, r := 2, num / 2
    for l <= r {
        m := (l + r) / 2
        squared := m * m
        if squared == num {
            return true
        }
        if squared > num {
            r = m - 1
        } else if squared < num {
            l = m + 1
        }
    }
    return false
}

func main() {

}