class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = (0, 0)
        for i, c in enumerate(s):
            radius = 0
            while (
                0 <= i - radius - 1 and i + radius + 1 < n
                and s[i - radius - 1] == s[i + radius + 1]
            ):
                radius += 1
            
            if res[1] - res[0] < radius * 2 + 1:
                res = (i - radius, i + radius + 1)
            
            radius = 0
            while (
                0 <= i - radius and i + radius + 1 < n
                and s[i - radius] == s[i + radius + 1]
            ):
                radius += 1
            
            if res[1] - res[0] < radius * 2:
                res = (i - radius + 1, i + radius + 1)

        return s[res[0]:res[1]]