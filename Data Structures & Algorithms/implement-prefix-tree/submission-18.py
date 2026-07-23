class PrefixNode:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None
        self.mid = None
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        char = word[i]
        if not node:
            node = PrefixNode(char)
        
        if char < node.char:
            node.left = self._insert(node.left, word, i)
        elif char > node.char:
            node.right = self._insert(node.right, word, i)
        elif i < len(word) - 1:
            node.mid = self._insert(node.mid, word, i+1)
        else:
            node.is_end = True
        
        return node

    def _get(self, node, word, i):
        if not node:
            return None
        
        char = word[i]
        if char < node.char:
            return self._get(node.left, word, i)
        elif char > node.char:
            return self._get(node.right, word, i)
        elif i < len(word) - 1:
            return self._get(node.mid, word, i+1)
        else:
            return node

    def search(self, word: str) -> bool:
        last = self._get(self.root, word, 0)
        return last is not None and last.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._get(self.root, prefix, 0) is not None
