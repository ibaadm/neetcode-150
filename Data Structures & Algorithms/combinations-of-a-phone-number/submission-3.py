class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        res = []
        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, curr):
            if i == n:
                res.append("".join(curr))
                return
            
            for char in digit_to_chars[digits[i]]:
                curr.append(char)
                dfs(i+1, curr)
                curr.pop()
        
        dfs(0, [])
        return res