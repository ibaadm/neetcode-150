from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l = 0
        max_freq = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])
            if r - l + 1 - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res