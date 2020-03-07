class TrieNode:
    def __init__(self):
        """
        TrieNode constructor.
        """
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        """
        Trie constructor.
        """
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children.get(char)
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Determines if word is in the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)
        return curr.end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Determines if there is any word in the trie that starts with the
        given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)
        return True
