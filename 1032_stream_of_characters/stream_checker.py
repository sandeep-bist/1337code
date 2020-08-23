class StreamChecker:

    def __init__(self, words: List[str]):
        """
        Time: O(m) where m is the length of the longest word
        Space: O(m)
        """
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie.root
        for char in self.stream:
            if node.end_of_word:
                return True
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.end_of_word


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

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
