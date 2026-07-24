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

        #so we have our current node and next node
        #we know the next node is checked otherwise we return early (doesnt exist)
        #if our current node doesnt have any other children, and our next node has
        #been fully checked and given the signal to be deleted
        #ok we delete that next node first, then check if there is no children
        #if so, then we give the signal that we should be deleted as well
        #whats the base case for this deletion
        #when adding ourselves to res, if we have no children, then give the signal to delete us
        #then we return early as well

        def dfs(node, r, c, used, word):
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
                    dfs(next_node, nr, nc, used, word)
            word.pop()
            used.remove((r, c))

            if not any(next_node.next):
                node.next[char_idx] = None

        res = []
        used = set()
        word = []
        for r in range(m):
            for c in range(n):
                dfs(root, r, c, used, word)

        return res