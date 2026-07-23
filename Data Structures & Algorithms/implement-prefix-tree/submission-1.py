class PrefixNode:
    def __init__(self):
        self.next = [None] * 26
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.head = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.next[idx]:
                curr.next[idx] = PrefixNode()
            curr = curr.next[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.next[idx]:
                return False
            curr = curr.next[idx]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.next[idx]:
                return False
            curr = curr.next[idx]
        return True
        