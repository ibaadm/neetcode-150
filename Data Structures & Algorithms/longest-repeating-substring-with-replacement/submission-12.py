from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        n = len(s)

        chars = {}
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = i

        for c, i in chars.items():
            l = max(0, i-k)
            r = l
            q = deque()
            while r < n:
                if s[r] != c:
                    if k == 0:
                        l = r+1
                    elif len(q) < k:
                        q.append(r)
                    else:
                        l = q.popleft() + 1
                        q.append(r)
                res = max(res, r-l+1)
                r += 1
        return res