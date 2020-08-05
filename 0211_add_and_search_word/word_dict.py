class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children.get(char)
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot
        character '.' to represent any one letter.
        """
        def find(word: str, node: TrieNode):
            if not word:
                return node.end_of_word
            char, word = word[0], word[1:]
            if char != '.':
                return char in node.children and find(word, node.children.get(char))
            return any(find(word, c) for c in node.children.values() if c)
        return find(word, self.root)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
