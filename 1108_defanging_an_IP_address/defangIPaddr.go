package main

import (
	"strings"
)

// Time: O(n)
// Space: O(n)
func defangIPaddr(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}

func main() {

}
