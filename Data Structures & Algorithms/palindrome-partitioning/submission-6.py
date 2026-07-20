import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_palindrome(string):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, curr):
            if i == n:
                if all(map(is_palindrome, curr)):
                    res.append(["".join(substring) for substring in curr])
                return

            if curr:
                curr[-1].append(s[i])
                dfs(i+1, curr)
                curr[-1].pop()

            curr.append([s[i]]) 
            dfs(i+1, curr)
            curr.pop()   
        
        dfs(0, [])
        return res