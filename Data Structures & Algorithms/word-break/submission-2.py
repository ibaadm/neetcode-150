class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for char in word:
                char_idx = ord(char) - ord('a')
                if curr.next[char_idx] is None:
                    curr.next[char_idx] = TrieNode()
                curr = curr.next[char_idx]
            curr.is_end = True
        
        n = len(s)
        visited = set()

        def recurse(i):
            if i in visited:
                return False
            visited.add(i)

            if i == n:
                return True
            
            curr = root
            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                if curr.next[char_idx] is None:
                    return False
                curr = curr.next[char_idx]
                if curr.is_end and recurse(j+1):
                    return True
            
            return False
        
        return recurse(0)