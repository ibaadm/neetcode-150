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
    
    #there may be a lot of repeated searching for consecutive .s
    def _search(self, node, word, i):
        if not node:
            return False
        
        if i == len(word):
            return node.is_end
        
        char = word[i]
        if char == '.':
            return any(self._search(node.next[j], word, i+1) for j in range(26))

        return self._search(node.next[ord(char) - ord('a')], word, i+1)
