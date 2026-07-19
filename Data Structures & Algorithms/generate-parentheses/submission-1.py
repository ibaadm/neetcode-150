class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, opens, closes):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            if opens < n:
                curr.append("(")
                dfs(curr, opens+1, closes)
                curr.pop()
            
            if closes < opens:
                curr.append(")")
                dfs(curr, opens, closes+1)
                curr.pop()
        
        dfs([], 0, 0)
        return res