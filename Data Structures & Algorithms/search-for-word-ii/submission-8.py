class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                idx = ord(char) - ord('a')
                if curr.next[idx] is None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.is_end = True

        def dfs(node, r, c):
            char = board[r][c]
            char_idx = ord(char) - ord('a')
            if node.next[char_idx] is None:
                return
            used.add((r, c))
            word.append(char)
            next_node = node.next[char_idx]
            if next_node.is_end:
                res.append("".join(word))
                next_node.is_end = False
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in used):
                    dfs(next_node, nr, nc)
            word.pop()
            used.remove((r, c))

            if not any(next_node.next):
                node.next[char_idx] = None

        res = []
        used = set()
        word = []
        for r in range(m):
            for c in range(n):
                dfs(root, r, c)

        return res