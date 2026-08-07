class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        res = [1, 0]

        for i in range(1, len(s)):
            temp = res[:]
            
            if s[i] == "0":
                res[0] = 0
            else:
                res[0] = temp[0] + temp[1]
            
            if s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6):
                res[1] = temp[0]
            else:
                res[1] = 0

        return sum(res)
