class TrieNode:
    def __init__(self, letter = ""):
        self.letter = letter
        self.children = {}
        self.mark = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node
        node.mark = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.mark
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)