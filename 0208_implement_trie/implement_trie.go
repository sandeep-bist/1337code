package main

type Trie struct {
	childMap map[byte]*Trie
	ending   bool
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{
		childMap: make(map[byte]*Trie),
		ending:   false,
	}
}

/** Inserts a word into the trie. */
func (t *Trie) Insert(word string) {
	if len(word) == 0 {
		return
	}
	currNode := t
	for i := 0; i < len(word); i++ {
		nextNode, ok := currNode.childMap[word[i]]
		if ok {
			currNode = nextNode
		} else {
			newNode := Constructor()
			currNode.childMap[word[i]] = &newNode
			currNode = &newNode
		}
	}
	currNode.ending = true
}

/** Returns if the word is in the trie. */
func (t *Trie) Search(word string) bool {
	if len(word) == 0 {
		return false
	}
	curr := t
	for i := 0; i < len(word); i++ {
		next, ok := curr.childMap[word[i]]
		if !ok {
			return false
		}
		curr = next
	}
	return curr.ending
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (t *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return true
	}
	curr := t
	for i := 0; i < len(prefix); i++ {
		next, ok := curr.childMap[prefix[i]]
		if !ok {
			return false
		}
		curr = next
	}
	return true
}

func main() {

}
