from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        
        window_count = defaultdict(int)
        have = 0
        need = len(t_count)
        res = None
        l = 0
        for r in range(len(s)):
            c = s[r]
            window_count[c] += 1
            if window_count[c] == t_count[c]:
                have += 1
            
            while have == need:
                if not res or res[1]-res[0] > r-l:
                    res = (l, r)
                
                c = s[l]
                if window_count[c] == t_count[c]:
                    have -= 1
                window_count[c] -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if res else ""
