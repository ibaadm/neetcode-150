class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        s1_counts = [0] * 26
        window_counts = [0] * 26
        for i in range(n):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_counts[i] <= window_counts[i]:
                matches += 1

        if matches == 26:
            return True
        
        for i in range(n, m):
            added_idx = ord(s2[i]) - ord('a')
            window_counts[added_idx] += 1
            if s1_counts[added_idx] == window_counts[added_idx]:
                matches += 1
            
            removed_idx = ord(s2[i-n]) - ord('a')
            window_counts[removed_idx] -= 1
            if s1_counts[removed_idx] == window_counts[removed_idx] + 1:
                matches -= 1

            if matches == 26:
                return True
        
        return False