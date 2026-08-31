class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res = []
        pending_chars = set()
        run = 0
        for c in s:
            pending_chars.add(c)
            count[ord(c) - ord('a')] -= 1
            run += 1

            if count[ord(c) - ord('a')] == 0:
                pending_chars.remove(c)
            
            if not pending_chars:
                res.append(run)
                run = 0
        
        return res