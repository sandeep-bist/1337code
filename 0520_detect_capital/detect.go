package main

import "strings"

// Time: O(n)
// Space: O(n)
func detectCapitalUse(word string) bool {
	return (strings.ToLower(word) == word ||
		strings.ToUpper(word) == word ||
		strings.ToLower(word[1:]) == word[1:])
}

func main() {

}
