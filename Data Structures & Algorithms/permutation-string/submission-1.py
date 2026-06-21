class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        s1_counts = [0] * 26
        for c in s1:
            s1_counts[ord(c) - ord('a')] += 1

        window_counts = [0] * 26
        for i in range(n):
            window_counts[ord(s2[i]) - ord('a')] += 1
        
        if window_counts == s1_counts:
            return True
        
        for i in range(n, m):
            window_counts[ord(s2[i]) - ord('a')] += 1
            window_counts[ord(s2[i-n]) - ord('a')] -= 1
            if window_counts == s1_counts:
                return True
        
        return False