class TrieNode {
  /**
   * TrieNode constructor.
   */
  constructor() {
    this.children = {}
    this.is_word = false
  }
}

class Trie {
  /**
   * Trie constructor.
   */
  constructor() {
    this.root = new TrieNode()
  }

  /**
   * Inserts a word into the trie.
   * @param     {string}    word
   */
  insert(word) {
    let curr = this.root
    for (let c of word) {
      if (!(c in curr.children)) curr.children[c] = new TrieNode()
      curr = curr.children[c]
    }
    curr.is_word = true
  }

  /**
   * Determines if word is in the trie.
   * @param     {string}    word
   * @returns   {boolean}
   */
  search(word) {
    let curr = this.root
    for (let c of word) {
      if (!(c in curr.children)) return false
      curr = curr.children[c]
    }
    return curr.is_word
  }

  /**
   * Determines if there is any word in the trie that starts with the
   * given prefix.
   * @param     {string}    word
   * @returns   {boolean}
   */
  startsWith(word) {
    let curr = this.root
    for (let c of word) {
      if (!(c in curr.children)) return false
      curr = curr.children[c]
    }
    return true
  }
}

const t = new Trie()
t.insert("hello")
t.insert("hey")
console.log(t.search("hello")) // true
console.log(t.search("hey")) // true
console.log(t.search("he")) // false
console.log(t.startsWith("he")) // true
