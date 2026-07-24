class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.next[idx]:
                curr.next[idx] = TrieNode()
            curr = curr.next[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)
    
    def _search(self, node, word, i):
        if not node:
            return False
        curr = node
        for j in range(i, len(word)):
            if word[j] == '.':
                return any(self._search(curr.next[k], word, j+1) for k in range(26))
            idx = ord(word[j]) - ord('a')
            if not curr.next[idx]:
                return False
            curr = curr.next[idx]
        return curr.is_end
