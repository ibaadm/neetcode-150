from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recurse(i, j):
            if j < 0:
                if i < 0:
                    return True
                return False

            if i < 0:
                return j > 0 and all(p[j] == '*' for k in range(1, j + 1, 2))
            
            if p[j] != '*':
                if s[i] == p[j] or p[j] == '.':
                    return recurse(i - 1, j - 1)
            else:
                if recurse(i, j - 2):
                    return True
                
                if p[j-1] == '.':
                    return any(recurse(k, j-2) for k in range(i - 1, -2, -1))

                for k in range(i, -1, -1):
                    if s[k] != p[j - 1]:
                        break

                    if recurse(k - 1, j - 2):
                        return True
            
            return False
        
        return recurse(len(s) - 1, len(p) - 1)
